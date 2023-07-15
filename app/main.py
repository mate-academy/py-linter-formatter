def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"], "column": error["column_number"],
        "message": error["text"], "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [{"line": error["line_number"],
                        "column": error["column_number"],
                        "message": error["text"], "name": error["code"],
                        "source": "flake8"} for error in errors],
            "path": file_path, "status": ("failed" if errors else "passed")}


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [{"line": line["line_number"],
                        "column": line["column_number"],
                        "message": line["text"], "name": line["code"],
                        "source": "flake8"} for line in value],
            "path": key,
            "status": ("failed" if value else "passed")
        }
        for key, value in linter_report.items()]
