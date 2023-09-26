def format_linter_error(error: dict) -> dict:
    return {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code"),
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [],
        "path": file_path,
        "status": "passed"
    } if errors == [] else {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(key, value) if value != [] else {

            "errors": value,

            "path": key,

            "status": "passed"

        }
        for key, value in linter_report.items()
    ]
