import pytest

from src.storage.base import VacancyStorage


def test_vacancy_storage_abstract_methods_raise_type_error() -> None:
    """
    Проверяет, что нельзя создать экземпляр класса,
    унаследованного от VacancyStorage без реализации абстрактных методов.
    """
    with pytest.raises(TypeError):

        class IncompleteStorage(VacancyStorage):
            pass

        IncompleteStorage()
