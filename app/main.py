def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    } if type(error) is dict else error


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors":
            [
                format_linter_error(error)
                for error in errors
                if type(error) is dict
            ],
        "path": file_path,
        "status": "failed" if len(errors) else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(
            file_path=error,
            errors=linter_report[error]
        )
        for error in linter_report
    ]