def format_linter_error(error: dict) -> dict:
    # write your code here
    return {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code"),
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # write your code here
    formatted_errors = []
    for error in errors:
        formatted_errors.append(format_linter_error(error))

    status = "failed" if formatted_errors else "passed"

    return {
        "path": file_path,
        "errors": formatted_errors,
        "status": status
    }


def format_linter_report(linter_report: dict) -> list:
    # write your code here
    output = []
    for file_path, errors in linter_report.items():
        error_list = [format_linter_error(error) for error in errors]
        status = "passed" if not error_list else "failed"
        output.append({
            "path": file_path,
            "errors": error_list,
            "status": status
        })
    return output
