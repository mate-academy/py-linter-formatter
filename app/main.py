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
            [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed" if errors else "passed"
    }  # why we cannot use here expression "... if errors is True else ..." ?


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file_path, errors)
        # if "path" != "passed" else
        # {"errors": [], "path": "path", "status": "passed"}
        for file_path, errors in linter_report.items()
    ]
