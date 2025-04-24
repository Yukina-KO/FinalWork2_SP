from typing import Dict, List, Optional


class Vacancy:
    """
    Класс, представляющий одну вакансию.
    Использует __slots__ для экономии памяти. Содержит основные поля,
    методы сравнения по зарплате и статический метод преобразования JSON-ответа от API.
    """

    __slots__ = ("title", "url", "salary", "description")

    def __init__(self, title: str, url: str, salary: Optional[int], description: str) -> None:
        """
        Инициализация объекта вакансии.
        Args:
            title (str): Название вакансии.
            url (str): Ссылка на вакансию.
            salary (Optional[int]): Зарплата (если None или некорректна — устанавливается 0).
            description (str): Краткое описание вакансии.
        """
        self.title = self._validate_str(title, "title")
        self.url = self._validate_str(url, "url")
        self.description = self._validate_str(description, "description")
        self.salary = self._validate_salary(salary)

    def _validate_str(self, value: Optional[str], field_name: str) -> str:
        """
        Проверяет, что значение является строкой.
        Args:
            value (Optional[str]): Значение для проверки.
            field_name (str): Название поля (для сообщения об ошибке).
        Returns:
            str: Исходное значение, если оно валидно.
        Raises:
            ValueError: Если значение не является строкой.
        """
        if not isinstance(value, str):
            raise ValueError(f"{field_name} должен быть строкой")
        return value

    def _validate_salary(self, salary: Optional[int]) -> int:
        """
        Валидирует зарплату.
        Args:
            salary (Optional[int]): Значение зарплаты.
        Returns:
            int: Валидированная зарплата (0, если не указана или < 0).
        """
        return salary if isinstance(salary, int) and salary > 0 else 0

    def __str__(self) -> str:
        """
        Строковое представление объекта вакансии.
        Returns:
            str: Форматированная строка с информацией о вакансии.
        """
        salary_str: str = f"{self.salary} руб." if self.salary else "Зарплата не указана"
        return f"{self.title} | {salary_str} | {self.url}"

    def __eq__(self, other: object) -> bool:
        """Проверка равенства по зарплате."""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary == other.salary

    def __lt__(self, other: object) -> bool:
        """Проверка «меньше» по зарплате."""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary < other.salary

    def __gt__(self, other: object) -> bool:
        """Проверка «больше» по зарплате."""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary > other.salary

    @staticmethod
    def cast_to_object_list(vacancies_data: List[Dict]) -> List["Vacancy"]:
        """
        Преобразует список словарей (данные с API) в список объектов Vacancy.
        Args:
            vacancies_data (List[Dict]): Список вакансий в формате JSON от hh.ru.
        Returns:
            List[Vacancy]: Список объектов класса Vacancy.
        """
        vacancies: List[Vacancy] = []
        for item in vacancies_data:
            title: str = item.get("name") or "Без названия"
            url: str = item.get("alternate_url") or "Нет ссылки"
            description: str = item.get("snippet", {}).get("requirement") or "Описание не указано"

            salary_info: Optional[Dict] = item.get("salary")
            salary: Optional[int] = None
            if salary_info and salary_info.get("from"):
                salary = salary_info["from"]

            vacancy = Vacancy(title=title, url=url, salary=salary, description=description)
            vacancies.append(vacancy)
        return vacancies

    def to_dict(self) -> Dict[str, str | int]:
        """
        Преобразует объект вакансии в словарь.
        Returns:
            Dict[str, str | int]: Словарь с полями вакансии.
        """
        return {"title": self.title, "url": self.url, "salary": self.salary, "description": self.description}
