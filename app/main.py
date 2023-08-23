def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [{"line": ers["line_number"],
                    "column": ers["column_number"],
                    "message": ers["text"], "name": ers["code"],
                    "source": "flake8"} for ers in errors],
        "path": file_path,
        "status": "failed" if errors else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [{"errors": [{"line": e["line_number"],
            "column": e["column_number"], "message": e["text"],
        "name": e["code"], "source": "flake8"} for e in errors],
        "path": file_path, "status": "failed" if errors else "passed"}
        for file_path, errors in linter_report.items()]
