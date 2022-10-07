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
                    "line": key["line_number"],
                    "column": key["column_number"],
                    "message": key["text"],
                    "name": key["code"],
                    "source": "flake8"
                }
                for key in errors
            ],
        "path": file_path,
        "status": "failed" if len(errors) > 1 else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "path": keys,
            "status": "failed" if len(linter_report[keys]) > 1 else "passed",
            "errors": [
                {
                    "line": key["line_number"],
                    "column": key["column_number"],
                    "message": key["text"],
                    "name": key["code"],
                    "source": "flake8"
                }
                for key in linter_report[keys]]
        }
        for keys in linter_report
    ]
