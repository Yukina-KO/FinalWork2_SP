# 📚 Документация классов проекта

Ниже приведён список всех классов проекта и их публичных/приватных методов.

---

## `JobAPI` (`src/api/base.py`)

| Метод | Тип | Назначение |
|-------|-----|------------|
| `get_vacancies(keyword: str) -> List[Dict[str, Any]]` | абстрактный | Получить список вакансий по ключевому слову |

---

## `HeadHunterAPI` (`src/api/hh.py`)

| Метод | Тип | Назначение |
|-------|-----|------------|
| `__init__()` | публичный | Инициализация, задаёт `_base_url` |
| `_fetch_from_api(params: Dict[str, str | int]) -> List[Dict[str, Any]]` | приватный | Отправляет запрос к API hh.ru и возвращает `items` |
| `get_vacancies(keyword: str) -> List[Dict[str, Any]]` | публичный | Формирует параметры запроса и вызывает `_fetch_from_api` |

---

## `Vacancy` (`src/models/vacancy.py`)

| Метод | Тип | Назначение |
|-------|-----|------------|
| `__init__(title, url, salary, description)` | публичный | Создаёт экземпляр вакансии, валидирует поля |
| `_validate_str(value, field_name)` | приватный | Проверка строковых параметров |
| `_validate_salary(salary)` | приватный | Нормализация зарплаты |
| `__str__()` | магический | Человекочитаемое представление |
| `__eq__(other)` | магический | Сравнение зарплат (равенство) |
| `__lt__(other)` | магический | Сравнение зарплат («меньше») |
| `__gt__(other)` | магический | Сравнение зарплат («больше») |
| `to_dict() -> Dict[str, str | int]` | публичный | Сериализация в словарь |
| `cast_to_object_list(vacancies_data) -> List[Vacancy]` | `@staticmethod` | Преобразование JSON‑данных API в объекты |

---

## `VacancyStorage` (`src/storage/base.py`)

| Метод | Тип | Назначение |
|-------|-----|------------|
| `add_vacancy(vacancy)` | абстрактный | Добавить вакансию |
| `get_vacancies()` | абстрактный | Получить все вакансии |
| `delete_vacancy(vacancy)` | абстрактный | Удалить вакансию |

---

## `JSONSaver` (`src/storage/json_saver.py`)

| Метод | Тип | Назначение |
|-------|-----|------------|
| `__init__(filepath: Optional[Path] = None)` | публичный | Инициализация, задаёт приватный `_filepath` |
| `add_vacancy(vacancy)` | публичный | Добавляет вакансию, избегая дублей |
| `get_vacancies() -> List[Vacancy]` | публичный | Читает файл и возвращает объекты |
| `delete_vacancy(vacancy)` | публичный | Удаляет вакансию из файла |
| `_read_data() -> List[Dict[str, Any]]` | приватный | Чтение JSON |
| `_write_data(data)` | приватный | Запись JSON |

---

## `TxtSaver` (`src/storage/txt_saver.py`)

| Метод | Тип | Назначение |
|-------|-----|------------|
| `__init__(filepath: Optional[Path] = None)` | публичный | Инициализация TXT‑файла |
| `add_vacancy(vacancy)` | публичный | Записывает строковое представление вакансии |
| `get_vacancies()` | публичный | (Заглушка) Возвращает пустой список |
| `delete_vacancy(vacancy)` | публичный | (Заглушка) Метод‑заглушка |

---

## Вспомогательные функции (`src/utils.py`)

| Функция | Назначение |
|---------|-----------|
| `filter_by_keywords(vacancies, keywords) -> List[Vacancy]` | Фильтр по ключевым словам |
| `filter_by_salary_range(vacancies, min_salary, max_salary) -> List[Vacancy]` | Фильтр по диапазону зарплат |

---
