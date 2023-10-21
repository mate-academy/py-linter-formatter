def format_linter_error(error: dict) -> dict:
    return {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code"),
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [
        {"line": i.get("line_number"),
         "column": i.get("column_number"),
         "message": i.get("text"),
         "name": i.get("code"),
         "source": "flake8"}
        for i in errors
    ],
        "path": file_path,
        "status": "failed",
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [
                {
                    "line": error["line_number"],
                    "column": error["column_number"],
                    "message": error["text"],
                    "name": error["code"],
                    "source": "flake8"
                }
                for error in value
            ] if value else [],
            "path": key,
            "status": "failed" if value else "passed"
        }
        for key, value in linter_report.items()
    ]
