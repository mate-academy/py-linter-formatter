def format_linter_error(error: dict) -> dict:
    return {"line": error.get("line_number"),
            "column": error.get("column_number"),
            "message": error.get("text"), "name": error.get("code"),
            "source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [{"line": error.get("line_number"),
                        "column": error.get("column_number"),
                        "message": error.get("text"),
                        "name": error.get("code"),
                        "source": "flake8"} for error in errors],
            "path": "./source_code_2.py",
            "status": "passed" if errors == [] else "failed"}


def format_linter_report(linter_report: dict) -> list:
    return [{"errors": [] if linter_report.get(file) == [] else [{
             "line": error.get("line_number"),
             "column": error.get("column_number"),
             "message": error.get("text"),
             "name": error.get("code"),
             "source": "flake8"} for error in linter_report.get(file)],
             "path": file,
             "status": "passed" if linter_report.get(file) == []
             else "failed"} for file in linter_report]
