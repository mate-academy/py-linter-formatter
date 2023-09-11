def format_linter_error(error: dict) -> dict:
    return {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code"),
        "source": "flake8",
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [
            {
                "line": error.get("line_number"),
                "column": error.get("column_number"),
                "message": error.get("text"),
                "name": error.get("code"),
                "source": "flake8",
            }
            for error in errors
        ],
        "path": "./source_code_2.py",
        "status": "failed",
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [
                {
                    "line": source.get("line_number"),
                    "column": source.get("column_number"),
                    "message": source.get("text"),
                    "name": source.get("code"),
                    "source": "flake8",
                }
                for source in value
            ],
            "path": key,
            "status": "passed" if value == [] else "failed",
        }
        for key, value in linter_report.items()
    ]
