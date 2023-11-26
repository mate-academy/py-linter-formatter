def format_linter_error(err: dict) -> dict:
    return {
        "line": err["line_number"],
        "column": err["column_number"],
        "message": err["text"],
        "name": err["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(val) for val in errors],
        "path": file_path,
        "status": "passed" if len(errors) == 0 else "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(key, value)
            for key, value in linter_report.items()]
