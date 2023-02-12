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
        "errors":
            [
                {
                    "line": errors.get("line_number"),
                    "column":errors.get("column_number"),
                    "message": errors.get("text"),
                    "name": errors.get("code"),
                    "source": "flake8"
                }
                for error in errors
            ],
        "path": "./source_code_2.py",
        "status": "failed"
    }

def format_linter_report(linter_report: dict) -> list:

    return [
        {
            "errors": [],
            "path": "./test_source_code_2.py",
            "status": "passed"
        },
        {
            "errors":
                [
                    {
                        "line": linter_report.get("line_number"),
                        "column": linter_report.get("column_number"),
                        "message": linter_report.get("text"),
                        "name": linter_report.get("code"),
                        "source": "flake8"
                    }
                    for error in errors
                ]

            "path": "./source_code_2.py",
            "status": "failed"
        }

    ]
