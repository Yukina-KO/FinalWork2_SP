from abc import ABC, abstractmethod
from typing import Dict, List


class JobAPI(ABC):
    """
    Абстрактный класс, представляющий интерфейс для API-сервисов, предоставляющих вакансии.
    Все классы, реализующие данный интерфейс, обязаны предоставить метод для получения вакансий
    по ключевому слову.
    Methods:
        get_vacancies(keyword: str) -> List[Dict]: Получает список вакансий по ключевому слову.
    """

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
