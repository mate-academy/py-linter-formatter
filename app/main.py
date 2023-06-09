def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }
    pass


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors":
            [
                {"line": error["line_number"],
                 "column": error["column_number"],
                 "message": error["text"],
                 "name": error["code"],
                 "source": "flake8"}

                for error in errors],

            "path": file_path,
            "status": "failed" if errors else "passed"
    }
    pass


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [
                {
                    "line": report["line_number"],
                    "column": report["column_number"],
                    "message": report["text"],
                    "name": report["code"],
                    "source": "flake8"
                }
                for report in reports
            ],
            "path": path,
            "status": "failed" if reports else "passed"
        }
        for path, reports in linter_report.items()
    ]
    pass
