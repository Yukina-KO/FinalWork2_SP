from typing import List

from src.models.vacancy import Vacancy


def filter_by_keywords(vacancies: List[Vacancy], keywords: List[str]) -> List[Vacancy]:
    """
    Фильтрует вакансии по ключевым словам, содержащимся в описании.
    Args:
        vacancies (List[Vacancy]): Список вакансий.
        keywords (List[str]): Список ключевых слов.
    Returns:
        List[Vacancy]: Отфильтрованные вакансии.
    """
    return [vacancy for vacancy in vacancies if any(word.lower() in vacancy.description.lower() for word in keywords)]


def filter_by_salary_range(vacancies: List[Vacancy], min_salary: int, max_salary: int) -> List[Vacancy]:
    """
    Фильтрует вакансии по диапазону зарплаты.
    Args:
        vacancies (List[Vacancy]): Список вакансий.
        min_salary (int): Нижняя граница зарплаты.
        max_salary (int): Верхняя граница зарплаты.
    Returns:
        List[Vacancy]: Отфильтрованные вакансии.
    """
    return [vacancy for vacancy in vacancies if min_salary <= vacancy.salary <= max_salary]
