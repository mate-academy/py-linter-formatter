def format_linter_error(error: dict) -> dict:
    # write your code here
    pass
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # write your code here
    pass
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    # write your code here
    pass
    return [
        {
            "errors": [format_linter_error(error) for error in errors],
            "path": file_path,
            "status": "failed" if errors else "passed"
        }
        for file_path, errors in linter_report.items()
    ]
