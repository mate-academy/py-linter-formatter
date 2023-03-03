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
        "errors": [
            format_linter_error(current_error)
            for current_error in errors if current_error["filename"]
            == file_path],
        "path": file_path,
        "status": "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [{
        "errors": (error_result := format_single_linter_file(file_name,
            error_list)["errors"]),
        "path": file_name,
        "status": "failed" if len(error_result) else "passed"
    } for file_name, error_list in linter_report.items()]
