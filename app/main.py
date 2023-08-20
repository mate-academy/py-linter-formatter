def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"error": [{"line": error["line_number"],
            "column": error["line_number"],
                       "message": error["column_number"],
                       "code": error["line_number"],
                       "source": "flake8"} for error in errors],
            "path": file_path,
            "status": ("failed" if len(errors) > 0 else "passed")}


def format_linter_report(linter_report: dict) -> list:
    return []
