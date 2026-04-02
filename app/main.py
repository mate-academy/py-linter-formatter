def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"], "column": error["column_number"], "message": error["text"],
            "name": error["code"], "source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> set:
    return {[{"line": error["line_number"], "column": error["column_number"], "message": error["text"],
            "name": error["code"], "source": "flake8"} for error in errors],
            {"path": file_path, "status": "passed" if len(errors) == 0 else "failed"}}


def format_linter_report(linter_report: dict) -> list:
    return [{{"errors": [], "path": linter_report["filename"], "status": "passed"},
            {"errors": [{
                    "line": 18,
                    "column": 80,
                    "message": "line too long (99 > 79 characters)",
                    "name": "E501",
                    "source": "flake8"
                },
                {
                    "line": 18,
                    "column": 100,
                    "message": "no newline at end of file",
                    "name": "W292",
                    "source": "flake8"}],
            {"path": linter_report["filename"], "status": "passed" if len("errors") == 0 else "failed"}}}] #показує помилку, що не вистачає : після ключа, але все стоїть на місці,в такому ж рядку 9 помилку не видає

