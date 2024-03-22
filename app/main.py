def format_linter_error(error: dict) -> dict:
    name = error.get("code", "")
    formatted_error = {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": name,
        "source": "flake8"
    }
    return formatted_error


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # write your code here
    pass


def format_linter_report(linter_report: dict) -> list:
    # write your code here
    pass
