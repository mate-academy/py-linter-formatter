def format_linter_error(error: dict) -> dict:
    return {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code"),
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [
            {
                "line": error.get("line_number"),
                "column": error.get("column_number"),
                "message": error.get("text"),
                "name": error.get("code"),
                "source": "flake8"
            }
            for error in errors
        ],
        "path": file_path,
        "status": "failed"
    }


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
                }
                for error in file_errors
            ] if file_errors else [],
            "path": file_path,
            "status": "passed" if not file_errors else "failed"
        }
        for file_path, file_errors in linter_report.items()
    ]
