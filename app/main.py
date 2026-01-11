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
                    "line": err_single_file["line_number"],
                    "column": err_single_file["column_number"],
                    "message": err_single_file["text"],
                    "name": err_single_file["code"],
                    "source": "flake8"
                } for err_single_file in errors

            ],
        "path": file_path,
        "status": "failed" if errors else "passed"
    }


def format_linter_report(linter_report: dict) -> list:

    return [
        {
            "errors": [
                {
                    "line": single_error["line_number"],
                    "column": single_error["column_number"],
                    "message": single_error["text"],
                    "name": single_error["code"],
                    "source": "flake8"
                } for single_error in file_errors
            ],
            "path": file,
            "status": "failed" if file_errors else "passed"
        } for file, file_errors in linter_report.items()
    ]
