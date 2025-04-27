from typing import Any, Dict, List, cast

import pytest

from src.models.vacancy import Vacancy


def test_vacancy_initialization() -> None:
    """
    Проверяет корректную инициализацию вакансии.
    """
    v = Vacancy("Python Dev", "http://example.com", 120000, "Опыт работы 3 года")
    assert v.title == "Python Dev"
    assert v.salary == 120000


def test_vacancy_salary_validation() -> None:
    """
    Проверяет установку зарплаты по умолчанию, если она не указана.
    """
    v = Vacancy("No Salary", "url", None, "desc")
    assert v.salary == 0


def test_vacancy_comparison() -> None:
    """
    Проверяет корректность сравнения вакансий по зарплате.
    """
    v1 = Vacancy("A", "url", 100000, "desc")
    v2 = Vacancy("B", "url", 200000, "desc")
    assert v2 > v1
    assert v1 < v2
    assert v1 != v2
    assert v1 == Vacancy("C", "url", 100000, "desc")


def test_vacancy_comparison_not_implemented() -> None:
    """
    Проверяет, что при сравнении с объектом другого типа выбрасывается TypeError.
    """
    v = Vacancy("Dev", "url", 100000, "desc")

    with pytest.raises(TypeError):
        _ = v > "строка"

    with pytest.raises(TypeError):
        _ = v < "строка"

    assert (v == "строка") is False


def test_vacancy_str() -> None:
    """
    Проверяет строковое представление вакансии.
    """
    v = Vacancy("Title", "http://example.com", None, "desc")
    assert "Зарплата не указана" in str(v)


def test_vacancy_cast_to_object_list() -> None:
    """
    Проверяет корректное преобразование данных API в список объектов Vacancy.
    """
    data: List[Dict] = [
        {"name": "Dev", "alternate_url": "http://url", "snippet": {"requirement": "Test"}, "salary": {"from": 100000}}
    ]
    result = Vacancy.cast_to_object_list(data)
    assert isinstance(result[0], Vacancy)
    assert result[0].salary == 100000


def test_vacancy_cast_to_object_list_with_missing_data() -> None:
    """
    Проверяет поведение cast_to_object_list при пропущенных значениях (без None).
    """
    data: List[Dict[str, Any]] = [{"snippet": {}, "salary": None}]
    result = Vacancy.cast_to_object_list(data)
    v = result[0]
    assert v.title == "Без названия"
    assert v.url == "Нет ссылки"
    assert v.description == "Описание не указано"
    assert v.salary == 0


def test_vacancy_invalid_types_raise() -> None:
    """
    Проверяет валидацию типов данных при инициализации.
    """
    with pytest.raises(ValueError):
        Vacancy(cast(Any, 123), "url", 1000, "desc")
    with pytest.raises(ValueError):
        Vacancy("Dev", cast(Any, 456), 1000, "desc")
    with pytest.raises(ValueError):
        Vacancy("Dev", "url", 1000, cast(Any, 789))
