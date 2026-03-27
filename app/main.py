def format_linter_error(error: dict) -> dict:
    return {
        "name": error["code"],
        "source": "flake8",
        "message": error["text"],
        "line": error["line_number"],
        "column": error["column_number"]
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [
            {
                "name": error["code"],
                "source": "flake8",
                "message": error["text"],
                "line": error["line_number"],
                "column": error["column_number"]
            } for error in errors
        ],
        "path": file_path,
        "status": "failed" if errors else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "path": path,
            "status": "passed" if not errors else "failed",
            "errors": [
                {
                    "name": error["code"],
                    "source": "flake8",
                    "message": error["text"],
                    "line": error["line_number"],
                    "column": error["column_number"]
                }
                for error in errors
            ]
        }
        for path, errors in linter_report.items()
    ]
