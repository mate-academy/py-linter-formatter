def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [
            {"line": error1["line_number"],
                "column": error1["column_number"],
                "message": error1["text"],
                "name": error1["code"],
                "source": "flake8"}
            for error1 in errors if error1["filename"] == file_path],
        "path": file_path, "status": "failed" if errors else "passed"}


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [] if not value1 else
            [
                {
                    "line": error2["line_number"],
                    "column": error2["column_number"],
                    "message": error2["text"],
                    "name": error2["code"],
                    "source": "flake8"}
                for error2 in value1],
            "path": key1,
            "status": "passed" if not value1 else "failed"
        }
        for key1, value1 in linter_report.items()
    ]
