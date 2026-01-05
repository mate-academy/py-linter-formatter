def format_linter_error(error: dict) -> dict:
    # write your code here
    pass
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8",
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # write your code here
    pass
    return {
        "path": file_path,
        "status": "passed" if not errors else "failed",
        "errors": [] if not errors else [
            format_linter_error(error) for error in errors
        ],
    }


def format_linter_report(linter_report: dict) -> list:
    # write your code here
    pass
    return [
        format_single_linter_file(path, errors)
        for path, errors in linter_report.items()
    ]
