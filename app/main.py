def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8" if "E" in error["code"] else "not_checked"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": []

    }


def format_linter_report(linter_report: dict) -> list:
    return
