from pathlib import Path
from src.api.hh import HeadHunterAPI
from src.models.vacancy import Vacancy
from src.storage.json_server import JSONSaver
from src.utils import filter_by_keywords, filter_by_salary_range


def user_interaction() -> None:
    """
    Основная функция взаимодействия с пользователем через консоль.
    Поддерживает:
    - ввод поискового запроса;
    - фильтрацию по ключевым словам;
    - фильтрацию по диапазону зарплат;
    - сортировку и отображение топ-N вакансий;
    - сохранение вакансий в JSON-файл.
    """
    api = HeadHunterAPI()
    storage = JSONSaver()  # По умолчанию: data/vacancies.json

    search_query: str = input("Введите поисковый запрос: ").strip()
    while True:
        try:
            top_n: int = int(input("Введите количество вакансий для отображения в топе: "))
            break
        except ValueError:
            print("❌ Пожалуйста, введите целое число.")
    filter_words = input("Введите ключевые слова для фильтрации описаний (через пробел): ").lower().split()

    salary_range_input = input("Введите диапазон зарплат (например, 50000-150000): ").replace(" ", "")
    min_salary, max_salary = 0, float("inf")
    if "-" in salary_range_input:
        parts = salary_range_input.split("-")
        if len(parts) == 2:
            try:
                min_salary = int(parts[0]) if parts[0].isdigit() else 0
                max_salary = int(parts[1]) if parts[1].isdigit() else float("inf")
            except ValueError:
                print("⚠️  Неверный формат диапазона. Диапазон не будет применён.")

    print("\nЗагружаю вакансии...\n")
    raw_vacancies = api.get_vacancies(search_query)
    vacancies = Vacancy.cast_to_object_list(raw_vacancies)

    # Сохраняем без дубликатов
    for v in vacancies:
        storage.add_vacancy(v)

    # Применение фильтров
    if filter_words:
        vacancies = filter_by_keywords(vacancies, filter_words)

    vacancies = filter_by_salary_range(vacancies, min_salary, max_salary)

    # Сортировка и топ N
    sorted_vacancies = sorted(vacancies, reverse=True)

    print(f"\nТоп-{top_n} вакансий:\n")
    for v in sorted_vacancies[:top_n]:
        print(v)


if __name__ == "__main__":
    user_interaction()
