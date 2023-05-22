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
    result_list = {
        "errors": errors,
        "path": file_path,
        "status": "failed" if errors else "passed",
    }

    return result_list


def format_linter_report(linter_report: dict) -> list:
    # write your code here
    return [format_single_linter_file(file_path=key, errors=value) for key, value in linter_report.items()]
