from unittest.mock import MagicMock, patch

import pytest

from src.api.hh import HeadHunterAPI


@patch("src.api.hh.requests.get")
def test_get_vacancies_success(mock_get: MagicMock) -> None:
    """
    Проверяет успешное получение вакансий с hh.ru.

    Args:
        mock_get (MagicMock): Замена requests.get.
    """
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"items": [{"name": "Python Dev"}]}

    api = HeadHunterAPI()
    result = api.get_vacancies("Python")
    assert isinstance(result, list)
    assert result[0]["name"] == "Python Dev"


@patch("src.api.hh.requests.get")
def test_get_vacancies_error(mock_get: MagicMock) -> None:
    """
    Проверяет, что при ошибке запроса вызывается исключение.
    Args:
        mock_get (MagicMock): Замена requests.get, имитирующая ошибку.
    """
    mock_get.return_value.raise_for_status.side_effect = Exception("Ошибка запроса")

    api = HeadHunterAPI()
    with pytest.raises(Exception):
        api.get_vacancies("Java")
