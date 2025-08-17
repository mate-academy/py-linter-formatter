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
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed"
    } if len(errors) > 0 else {
        "path": file_path,
        "status": "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [],
            "path": linter,
            "status": "passed"
        } if len(linter_report[linter]) == 0 else
        format_single_linter_file(linter, linter_report[linter])
        for linter in linter_report
    ]
