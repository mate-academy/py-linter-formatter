def format_linter_error(error: dict) -> dict:
    return {"line": error.get("line_number"),
            "column": error.get("column_number"),
            "message": error.get("text"),
            "name": error.get("code"),
            "source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return ({
        "errors": [
            {
                "line": error.get("line_number"),
                "column": error.get("column_number"),
                "message": error.get("text"),
                "name": error.get("code"),
                "source": "flake8"
            } for error in errors
        ],
        "path": file_path,
        "status": "passed" if not errors else "failed"
    } if file_path else {})


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [
                {
                    "line": error.get("line_number"),
                    "column": error.get("column_number"),
                    "message": error.get("text"),
                    "name": error.get("code"),
                    "source": "flake8"
                } for error in linter_report[file_path]
            ],
            "path": file_path,
            "status": "passed" if not linter_report[file_path] else "failed"
        } for file_path in linter_report
    ]
