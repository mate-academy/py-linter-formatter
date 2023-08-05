def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(error) for error in errors],
        "status": "failed" if errors else "passed",
        "path": file_path
    }
# відрагувати кожну помилку використовуючи функцію format_linter_error


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(path, errors)
        for path, errors in linter_report.items()
    ]

# треба проітеруватися по format_linter_error.items
# for path, errors in linter_report.items()
# до errors треба функцію format_single_linter_file
