def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"],
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
                    "line": dictionary["line_number"],
                    "column": dictionary["column_number"],
                    "message": dictionary["text"],
                    "name": dictionary["code"],
                    "source": "flake8"
                }
                for dictionary in errors
            ],
        "path": file_path,
        "status": "passed" if errors == [] else "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [
                {
                    "line": dicts["line_number"],
                    "column": dicts["column_number"],
                    "message": dicts["text"],
                    "name": dicts["code"],
                    "source": "flake8"
                } for dicts in value
            ],
            "path": key,
            "status": "passed" if linter_report[key] == [] else "failed"
        } for key, value in linter_report.items()
    ]
