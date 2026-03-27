def format_linter_error(error: dict) -> dict:
    # Преобразуем данные из "line_number" и "column_number" в "line" и "column"
    return {
        "line": int(error["line_number"]),       # Используем "line_number" для "line"
        "column": int(error["column_number"]),   # Используем "column_number" для "column"
        "message": str(error["text"]),           # Используем "text" для сообщения об ошибке
        "name": error["code"],                   # Код ошибки из "code"
        "source": "flake8"                       # Добавляем источник
    }

def format_single_linter_file(file_path: str, errors: list) -> dict:
    # Функция должна содержать только один return
    return {
        "path": file_path,                       # Путь к файлу
        "errors": [format_linter_error(error) for error in errors],  # Список отформатированных ошибок
        "status": "failed" if errors else "passed"  # Статус: "failed" если ошибки, иначе "passed"
    }

def format_linter_report(errors_linter: dict) -> list:
    # Функция должна содержать только один return
    return [
        format_single_linter_file(file_path, errors)
        for file_path, errors in errors_linter.items()
    ]