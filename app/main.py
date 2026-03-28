def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"], "column": error["column_number"],
        "message": error["text"], "name": error["code"], "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors":
            [
                {
                    "line": single_error["line_number"],
                    "column": single_error["column_number"],
                    "message": single_error["text"],
                    "name": single_error["code"],
                    "source": "flake8"
                } for single_error in errors
            ], "path": file_path, "status": "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [
                {
                    "line": errors["line_number"],
                    "column": errors["column_number"],
                    "message": errors["text"],
                    "name": errors["code"],
                    "source": "flake8",
                } for errors in linter_report[file_report]
            ],
            "path": file_report,
            "status":
                "failed" if len(linter_report[file_report]) != 0 else "passed"
        } for file_report in linter_report
    ]
