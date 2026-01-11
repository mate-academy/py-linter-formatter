def format_linter_error(error: dict) -> dict:
    return {
        "line": error.pop("line_number"),
        "column": error.pop("column_number"),
        "message": error.pop("text"),
        "name": error.pop("code"),
        "source": "flake8"
    }


pass


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed" if errors else "passed",

    }

    pass


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file_path, errors) for file_path, errors in linter_report.items() # noqa

    ]

    pass
