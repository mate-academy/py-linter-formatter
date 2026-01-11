def format_linter_error(error: dict) -> dict:
    return {
        "name": error["code"],
        "line": error["line_number"],
        "message": error["text"],
        "column": error["column_number"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "path": file_path,
        "status": "failed" if errors else "passed",
        "errors": [format_linter_error(error) for error in errors]
    }


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(file_path, errors)
            for file_path, errors in linter_report.items()]
