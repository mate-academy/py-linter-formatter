def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    


def format_linter_report(linter_report: dict) -> list:
    # white your code here
    pass
