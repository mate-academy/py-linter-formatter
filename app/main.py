def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }
    # створює словник зі зміненими ключами та додатковим полем


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status":
            "failed" if errors else "passed"
    }
    # в "errors" записує, змінену попередньою функцією, інформацію з errors
    # в "path" передає шлях файлу з file_path
    # в "status" передає інформацію чи є взагалі помилка


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file_path, errors)
        for file_path, errors in linter_report.items()
    ]
    # форматує всі помилки для всіх файлів звіту
