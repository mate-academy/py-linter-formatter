def format_linter_error(error: dict) -> dict:
    # white your code here
    # return [
    # {"errors": value,
    # "path": key,
    # "status": "passed" if value == [] else "failed"}
    # for key, value in error.items()]
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # white your code here
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "passed" if len(errors) == 0 else "failed"}


def format_linter_report(linter_report: dict) -> list:
    # white your code here
    return [
        format_single_linter_file(file_path, errors)
        for file_path, errors in linter_report.items()
    ]
