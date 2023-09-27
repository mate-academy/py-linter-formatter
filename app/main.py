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
                "line": errors[0]["line_number"],
                "column": errors[0]["column_number"],
                "message": errors[0]["text"],
                "name": errors[0]["code"],
                "source": "flake8"
            },
            {
                "line": errors[1]["line_number"],
                "column": errors[1]["column_number"],
                "message": errors[1]["text"],
                "name": errors[1]["code"],
                "source": "flake8"
            }
        ],
        "path": "./source_code_2.py",
        "status": "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "path": path,
            "status": "passed" if not errors else "failed",
            "errors": [
                {
                    "line": error["line_number"],
                    "column": error["column_number"],
                    "message": error["text"],
                    "name": error["code"],
                    "source": "flake8"
                }
                for error in errors
            ]
        }
        for path, errors in linter_report.items()
    ]
