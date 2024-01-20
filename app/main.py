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
        "errors":
            [
                format_linter_error(error)
                for error in errors
            ],
        "path": file_path,
        "status": "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [],
            "path": key,
            "status": "passed"
        } if len(value) == 0 else
        format_single_linter_file(file_path=key, errors=value)
        for key, value in linter_report.items()
    ]
