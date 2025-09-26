def format_linter_error(error: dict) -> dict:
    # Функція, що форматує одну помилку
    return {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code"),
        "source": "flake8",
    }

# 1. Створюємо тестовий словник з помилкою
test_error = {
    "line_number": 10,
    "column_number": 5,
    "text": "Indentation is not a multiple of four",
    "code": "E111",
    "filename": "some/file.py" # Цей ключ ігнорується
}

# 2. Створюємо очікуваний результат
expected_result = {
    "line": 10,
    "column": 5,
    "message": "Indentation is not a multiple of four",
    "name": "E111",
    "source": "flake8"
}

# 3. Робимо простий assert для перевірки
assert format_linter_error(test_error) == expected_result

print("✅ Крок 1: Тест для format_linter_error пройдено успішно!")
