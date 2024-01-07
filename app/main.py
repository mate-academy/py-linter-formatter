def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8",
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [
            {format_linter_key: format_linter_value
                for format_linter_key, format_linter_value
                in format_linter_error(one_error).items()}
            for one_error in errors
        ],
        "path": file_path,
        "status": "failed" if len(errors) > 0 else "passed",
    }


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(linter_report_key,
                                      linter_report_value)
            for linter_report_key, linter_report_value
            in linter_report.items()]
