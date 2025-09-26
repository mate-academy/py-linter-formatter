def format_linter_error(error: dict) -> dict:
    """
    Форматує один словник з помилкою, приводячи його до стандартизованого вигляду.
    Використовує .get() для безпечного доступу до даних.
    """
    return {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code"),
        "source": "flake8",
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    """
    Форматує звіт для одного файлу: створює список помилок,
    встановлює шлях та визначає статус.
    """
    return {
        "errors": [format_linter_error(err) for err in errors],
        "path": file_path,
        "status": "passed" if not errors else "failed",
    }


def format_linter_report(linter_errors: dict) -> list:
    """
    Створює фінальний звіт у вигляді списку, форматуючи дані
    для кожного файлу з вхідного словника.
    """
    return [
        format_single_linter_file(path, file_errors)
        for path, file_errors in linter_errors.items()
    ]
