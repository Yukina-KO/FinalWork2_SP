from abc import ABC, abstractmethod
from typing import List

from src.models.vacancy import Vacancy


class VacancyStorage(ABC):
    """
    Абстрактный класс для хранилищ вакансий.
    Определяет интерфейс для добавления, удаления и получения вакансий.
    Позволяет заменить реализацию (файл, база данных, API и т.д.).
    """

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        """
        Добавить вакансию в хранилище.
        Args:
            vacancy (Vacancy): Объект вакансии для сохранения.
        """
        pass

    @abstractmethod
    def get_vacancies(self) -> List[Vacancy]:
        """
        Получить все вакансии из хранилища.
        Returns:
            List[Vacancy]: Список объектов вакансий.
        """
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """
        Удалить вакансию из хранилища.
        Args:
            vacancy (Vacancy): Объект вакансии, который нужно удалить.
        """
        pass
