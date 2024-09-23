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
        "errors": [
            {
                "line": error["line_number"],
                "column": error["column_number"],
                "message": error["text"],
                "name": error["code"],
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
            "errors": [],
            "path": filepath,
            "status": "passed"
        } if not issues else {
            "errors": [
                {
                    "line": issue["line_number"],
                    "column": issue["column_number"],
                    "message": issue["text"],
                    "name": issue["code"],
                    "source": "flake8"
                }
                for issue in issues
            ],
            "path": filepath,
            "status": "failed"
        } for filepath, issues in linter_report.items()
    ]
