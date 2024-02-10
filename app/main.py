def format_linter_error(error: dict) -> dict:
    # write your code here
    return {"line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "source": "flake8"
            }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # write your code here
    status = "failed" if any(error["code"].startswith("E") for error in errors) else "passed"
    formatted_errors = [{
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    } for error in errors]
    return {
        "errors": formatted_errors,
        "path": file_path,
        "status": status
    }

def format_linter_report(linter_report: dict) -> list:
    # write your code here
    pass
