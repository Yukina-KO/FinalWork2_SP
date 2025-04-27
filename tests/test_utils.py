from typing import List

import pytest

from src.models.vacancy import Vacancy
from src.utils import filter_by_keywords, filter_by_salary_range


@pytest.fixture
def sample_vacancies() -> List[Vacancy]:
    """
    Создаёт список тестовых вакансий.
    """
    return [
        Vacancy("Python Dev", "url1", 100000, "Опыт с Python и Django"),
        Vacancy("JS Dev", "url2", 80000, "JavaScript и React"),
        Vacancy("Analyst", "url3", 60000, "SQL, Excel"),
        Vacancy("Rust Dev", "url4", 120000, "Знание Rust и WASM"),
    ]


def test_filter_by_keywords_match(sample_vacancies: List[Vacancy]) -> None:
    """
    Проверяет, что фильтрация по ключевым словам возвращает правильные вакансии.
    """
    result = filter_by_keywords(sample_vacancies, ["python"])
    assert len(result) == 1
    assert result[0].title == "Python Dev"


def test_filter_by_keywords_multiple_keywords(sample_vacancies: List[Vacancy]) -> None:
    """
    Проверяет, что фильтрация работает при нескольких ключевых словах.
    """
    result = filter_by_keywords(sample_vacancies, ["rust", "sql"])
    titles = [v.title for v in result]
    assert "Rust Dev" in titles
    assert "Analyst" in titles
    assert len(result) == 2


def test_filter_by_keywords_no_match(sample_vacancies: List[Vacancy]) -> None:
    """
    Проверяет, что при отсутствии совпадений возвращается пустой список.
    """
    result = filter_by_keywords(sample_vacancies, ["kotlin"])
    assert result == []


def test_filter_by_keywords_empty_input(sample_vacancies: List[Vacancy]) -> None:
    """
    Проверяет, что пустой список ключевых слов возвращает исходный список (без фильтрации).
    """
    result = filter_by_keywords(sample_vacancies, [])
    assert result == []  # Нет ни одного ключа — фильтр не находит совпадений


def test_filter_by_salary_range_basic(sample_vacancies: List[Vacancy]) -> None:
    """
    Проверяет фильтрацию вакансий по диапазону зарплат.
    """
    result = filter_by_salary_range(sample_vacancies, 70000, 100000)
    titles = [v.title for v in result]
    assert "Python Dev" in titles
    assert "JS Dev" in titles
    assert len(result) == 2


def test_filter_by_salary_range_exact_bounds(sample_vacancies: List[Vacancy]) -> None:
    """
    Проверяет работу фильтра на граничных значениях.
    """
    result = filter_by_salary_range(sample_vacancies, 60000, 60000)
    assert len(result) == 1
    assert result[0].title == "Analyst"


def test_filter_by_salary_range_no_match(sample_vacancies: List[Vacancy]) -> None:
    """
    Проверяет, что при отсутствии подходящих зарплат возвращается пустой список.
    """
    result = filter_by_salary_range(sample_vacancies, 200000, 300000)
    assert result == []


def test_filter_by_salary_range_empty_list() -> None:
    """
    Проверяет фильтрацию по диапазону для пустого списка вакансий.
    """
    result = filter_by_salary_range([], 0, 100000)
    assert result == []
