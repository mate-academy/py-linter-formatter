def format_linter_error(error: dict) -> dict:
    """
    Форматує одну помилку лінтера, щоб включити лише певні ключі.
    """
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8",
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    """
    Форматує звіт для одного файлу.
    """
    formatted_errors = [format_linter_error(error) for error in errors]
    return {
        "errors": formatted_errors,
        "path": file_path,
        "status": "passed" if not formatted_errors else "failed",
    }


def format_linter_report(linter_errors: dict) -> list:
    """
    Форматує повний звіт лінтера.
    """
    return [
        format_single_linter_file(path, file_errors)
        for path, file_errors in linter_errors.items()
    ]
