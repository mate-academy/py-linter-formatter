def format_linter_error(error: dict) -> dict:
    """
    Преобразует одну ошибку из формата линтера в плоский словарь.
    """
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "code": error["code"],
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    """
    Форматирует все ошибки для одного конкретного файла.
    """
    return {
        "errors": [format_linter_error(e) for e in errors],
        "path": file_path,
        "status": "failed" if errors else "passed",
    }


def format_linter_report(linter_report: dict) -> list:
    """
    Преобразует весь отчет линтера в итоговый список.
    """
    return [
        format_single_linter_file(path, errors)
        for path, errors in linter_report.items()
    ]

