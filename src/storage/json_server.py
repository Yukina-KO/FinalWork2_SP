import json
from pathlib import Path
from typing import Any, List, Optional

from src.models.vacancy import Vacancy
from src.storage.base import VacancyStorage


class JSONSaver(VacancyStorage):
    """
    Класс для сохранения вакансий в JSON-файл.
    Использует список вакансий, сериализуемый в JSON.
    """

    def __init__(self, filepath: Optional[Path] = None) -> None:
        """
        Инициализация JSONSaver с путем к файлу.
        Args:
            filepath (Optional[Path]): Путь к JSON-файлу.
                Если не указан — используется путь по умолчанию "data/vacancies.json".
        """
        self._filepath: Path = filepath or Path("data/vacancies.json")
        self._filepath.parent.mkdir(parents=True, exist_ok=True)
        if not self._filepath.exists():
            self._filepath.write_text("[]", encoding="utf-8")

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """
        Добавляет вакансию в JSON-файл.
        Args:
            vacancy (Vacancy): Объект вакансии.
        """
        data = self._read_data()
        vacancy_dict = vacancy.to_dict()

        if vacancy_dict not in data:
            data.append(vacancy_dict)
            self._write_data(data)

    def get_vacancies(self) -> List[Vacancy]:
        """
        Получить все вакансии из файла.
        Returns:
            List[Vacancy]: Список объектов Vacancy.
        """
        data = self._read_data()
        return [Vacancy(**item) for item in data]

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """
        Удаляет вакансию из файла по совпадению всех полей.
        Args:
            vacancy (Vacancy): Объект для удаления.
        """
        data = self._read_data()
        filtered = [item for item in data if item != vacancy.to_dict()]
        self._write_data(filtered)

    def _read_data(self) -> List[dict]:
        """Читает и возвращает содержимое JSON-файла."""
        with self._filepath.open("r", encoding="utf-8") as file:
            data: Any = json.load(file)
            return data if isinstance(data, list) else []

    def _write_data(self, data: List[dict]) -> None:
        """Записывает список словарей в JSON-файл."""
        with self._filepath.open("w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
