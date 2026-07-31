def format_linter_error(error: dict) -> dict:
    return {key_error: key for key_error, key in {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code"),
        "source": "flake8"
    }.items()}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [
            {key_error: key for key_error, key in {
                "line": error.get("line_number"),
                "column": error.get("column_number"),
                "message": error.get("text"),
                "name": error.get("code"),
                "source": "flake8"
            }.items()}
            for error in errors
        ],
        "path": file_path,
        "status": "failed" if errors != [] else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [
                {key_error: key for key_error, key in {
                    "line": error.get("line_number"),
                    "column": error.get("column_number"),
                    "message": error.get("text"),
                    "name": error.get("code"),
                    "source": "flake8"
                }.items()}
                for error in value
            ],
            "path": key,
            "status": "failed" if value != [] else "passed"
        } for key, value in linter_report.items()
    ]
