def correct_name_dict() -> dict:
    return {
        "line_number": "line",
        "code": "name",
        "column_number": "column",
        "text": "message",
    }


def format_linter_error(error: dict) -> dict:
    return {
        correct_name_dict().get(key, "source"): value
        if key in correct_name_dict()
        else ("flake8" if key == "source" else "flake8")
        for key, value in error.items()
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "passed" if not errors else "failed",
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file, errors)
        for file, errors in linter_report.items()
    ]
