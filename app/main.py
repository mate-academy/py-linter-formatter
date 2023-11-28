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
            "errors": next(iter(linter_report)),
            "path": linter_report[next(iter(linter_report))],
            "status": "passed"
        },
        {
            "errors":
                [
                    {
                        "line": error["line_number"],
                        "column": error["column_number"],
                        "message": error["text"],
                        "name": error["code"],
                        "source": "flake8"
                    }
                    for error in linter_report[next(iter(linter_report))]
                ],
            "path": "./source_code_2.py",
            "status": "failed"
        }
    ]
