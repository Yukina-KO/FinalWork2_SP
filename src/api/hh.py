from typing import Any, Dict, List

import requests

from src.api.base import JobAPI


class HeadHunterAPI(JobAPI):
    """
    Класс для работы с API hh.ru.
    """

    def __init__(self) -> None:
        """
        Инициализация API-клиента hh.ru.
        """
        self.__base_url: str = "https://api.hh.ru/vacancies"

    def _fetch_from_api(self, params: Dict[str, str | int]) -> List[Dict[str, Any]]:
        """
        Реализация абстрактного метода для обращения к API hh.ru.
        Args:
            params (Dict[str, str | int]): Параметры запроса.
        Returns:
            List[Dict]: Список словарей-вакансий.
        """
        response = requests.get(self.__base_url, params=params)
        response.raise_for_status()
        response_json: Dict[str, Any] = response.json()

        items: Any = response_json.get("items", [])
        if not isinstance(items, list):
            return []

        return items

    def get_vacancies(self, keyword: str) -> List[Dict]:
        """
        Реализация абстрактного метода для получения списка вакансий с hh.ru по ключевому слову.
        Args:
            keyword (str): Ключевое слово для поиска (например, "Python Developer").
        Returns:
            List[Dict]: Список словарей с описанием вакансий, полученных с hh.ru.
        Raises:
            requests.exceptions.HTTPError: В случае, если запрос завершился с ошибкой.
        """
        params: Dict[str, str | int] = {"text": keyword, "area": 113, "per_page": 100}
        return self._fetch_from_api(params)
