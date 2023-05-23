def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"], "column": error["column_number"], "message": error["text"],
            "name": error["code"], "source": "flake8"}
    pass


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [{"line": error["line_number"], "column": error["column_number"], "message": error["text"],
                        "name": error["code"], "source": "flake8"} for error in errors],
            "path": file_path, "status": "passed" if not errors else "failed"}
    pass


def format_linter_report(linter_report: dict) -> list:
    return [{"errors": error if not error else [
        {"line": errors["line_number"], "column": errors["column_number"], "message": errors["text"],
         "name": errors["code"], "source": "flake8"} for errors in error],
             "path": name, "status": "passed" if not error else "failed"} for name, error in linter_report.items()]
    pass
