def format_linter_error(error: dict) -> dict:
    # write your code here
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }



def format_single_linter_file(file_path: str, errors: list) -> dict:
    # write your code here
    return {
        file_path: [format_linter_error(err) for err in errors]
    }



def format_linter_report(linter_report: dict) -> list:
    # write your code here
    formatted = []
    for file_path, errors in linter_report.items():
        formatted.append(format_single_linter_file(file_path, errors))
    return formatted
