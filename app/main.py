def format_linter_error(error: dict) -> dict:
    return {
        "message": error.get("text", ""),
        "line": error.get("line_number", 0),
        "column": error.get("column_number", 0)
    }
    pass


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        file_path: [format_error_item(error) for error in errors]
    }
    pass


def format_linter_report(linter_report: dict) -> list:
    return [
        _format_error_item(error)
        for file_path, errors in linter_report.items()  # 1. Перебираємо пари (файл, список помилок)
        for error in errors  # 2. Перебираємо кожну помилку у списку
    ]
