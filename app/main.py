# from statistics import pstdev


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
        "errors" : [format_linter_error(er) for er in errors],
        "path" : file_path,
        "status" : "failed" if errors else "passed"}


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(path, er)
        for path, er in linter_report.items()]
