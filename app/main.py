def format_linter_error(error: dict) -> dict:
    """
    Форматує одну помилку лінтера, щоб включити лише певні ключі.
    """
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["message"],
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    """
    Форматує звіт лінтера для одного файлу.
    """
    formatted_errors = [format_linter_error(error) for error in errors]
    return {
        "file_path": file_path,
        "errors": formatted_errors,
    }


def format_linter_report(linter_report: dict) -> list:
    """
    Форматує повний звіт лінтера для всіх файлів.
    """
    return [
        format_single_linter_file(path, errors)
        for path, errors in linter_report.items()
    ]
    return [
        format_single_linter_file(path, errors)
        for path, errors in linter_report.items()
    ]
