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
        "errors":
            [
                {
                    "line": dc["line_number"],
                    "column": dc["column_number"],
                    "message": dc["text"],
                    "name": dc["code"],
                    "source": "flake8"
                }
                for dc in errors
            ],
        "path": file_path,
        "status": "failed" if any(errors) else "passed"
    }


def format_linter_report(linter_report: dict) -> list:

    return [
        {
            "errors":
                [
                    {
                        "line": elem["line_number"],
                        "column": elem["column_number"],
                        "message": elem["text"],
                        "name": elem["code"],
                        "source": "flake8"
                    }
                    for elem in val
                ]
            if all(val) else [],
            "path": key,
            "status":"failed" if any(val)
            else "passed"
        }
        for key, val in linter_report.items()
    ]

