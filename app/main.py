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
                    "line": error["line_number"],
                    "column": error["column_number"],
                    "message": error["text"],
                    "name": error["code"],
                    "source": "flake8"
                }
                for error in errors
            ],
        "path": file_path,
        "status": "failed" if errors else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [
                {
                    "line": report_value["line_number"],
                    "column": report_value["column_number"],
                    "message": report_value["text"],
                    "name": report_value["code"],
                    "source": "flake8"
                }
                for report_value in report_value_list
            ],
            "path": key_report,
            "status": "failed" if report_value_list else "passed"
        }
        for key_report, report_value_list in linter_report.items()
    ]
