def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [{"line": element["line_number"],
                        "column": element["column_number"],
                        "message": element["text"],
                        "name": element["code"],
                        "source": "flake8"} for element in errors],
            "path": file_path,
            "status": "failed"}


def format_linter_report(linter_report: dict) -> list:
    return [{"errors": [] if not errors else [
        {"line": e["line_number"],
         "column": e["column_number"],
         "message": e["text"],
         "name": e["code"],
         "source": "flake8"}
        for e in errors],
        "path": file_path,
        "status": "passed" if not errors else "failed"}
        for file_path, errors in linter_report.items()]
