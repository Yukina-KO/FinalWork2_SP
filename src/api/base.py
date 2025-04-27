from abc import ABC, abstractmethod
from typing import Dict, List, Any


class JobAPI(ABC):
    """
    Абстрактный класс, представляющий интерфейс для API-сервисов, предоставляющих вакансии.
    Все классы, реализующие данный интерфейс, обязаны предоставить метод для получения вакансий
    по ключевому слову.
    Methods:
        get_vacancies(keyword: str) -> List[Dict]: Получает список вакансий по ключевому слову.
        _fetch_from_api(params: Dict[str, str | int]): Метод для подключения к API
    """
    @abstractmethod
    def _fetch_from_api(self, params: Dict[str, str | int]) -> List[Dict[str, Any]]:
        """
        Абстрактный метод для запроса к API.
        Args:
            params (Dict[str, str | int]): Параметры запроса.
        Returns:
            List[Dict[str, Any]]: Список словарей с данными о вакансиях.
        """
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str) -> List[Dict]:
        """
        Получить список вакансий по заданному ключевому слову.
        Args:
            keyword (str): Ключевое слово для поиска вакансий (например, "Python").
        Returns:
            List[Dict]: Список словарей, каждый из которых содержит информацию о вакансии.
        """
        pass
