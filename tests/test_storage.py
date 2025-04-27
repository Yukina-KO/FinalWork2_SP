import tempfile
from pathlib import Path

from src.models.vacancy import Vacancy
from src.storage.json_server import JSONSaver


def test_json_saver_add_get_delete() -> None:
    """
    Проверяет добавление, чтение и удаление вакансий из JSON-файла.
    """
    with tempfile.TemporaryDirectory() as tmp:
        file = Path(tmp) / "vacancies.json"
        storage = JSONSaver(file)

        v = Vacancy("Test Dev", "http://link", 90000, "Описание")
        storage.add_vacancy(v)

        vacancies = storage.get_vacancies()
        assert len(vacancies) == 1
        assert vacancies[0].title == "Test Dev"

        storage.delete_vacancy(v)
        assert storage.get_vacancies() == []
