def format_linter_error(error: dict) -> dict:
    return {"line": error.get("line_number"),
            "column": error.get("column_number"),
            "message": error.get("text"),
            "name": error.get("code"),
            "source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [{"line": mis.get("line_number"),
                        "column": mis.get("column_number"),
                        "message": mis.get("text"),
                        "name": mis.get("code"),
                        "source": "flake8"} for mis in errors],
            "path": file_path,
            "status": "failed" if len(errors) else "passed"}


def format_linter_report(linter_report: dict) -> list:
    return [{"errors": [{"line": mis.get("line_number"),
                         "column": mis.get("column_number"),
                         "message": mis.get("text"),
                         "name": mis.get("code"),
                         "source": "flake8"} for mis in value],
            "path": key, "status": "failed" if value else "passed"}
            for key, value in linter_report.items()]
