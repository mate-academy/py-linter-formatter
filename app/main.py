def format_linter_error(error: dict) -> dict:
    formatted_error = {
        "line": error.get("line"),
        "column": error.get("column"),
        "message": error.get("message"),
        "name": error.get("name"),
        "source": error.get("source"),
    }
    return formatted_error


def format_single_linter_file(file_path: str, errors: list) -> dict:
    formatted_errors = []
    for error in errors:
        formatted_errors.append(format_linter_error(error))

    return {
        "errors": formatted_errors,
        "path": file_path,
        "status": "failed" if formatted_errors else "passed",
    }


def format_linter_report(linter_report: dict) -> list:
    formatted_results = []
    for file_path, errors in linter_report.items():
        formatted_file = format_single_linter_file(file_path, errors)
        formatted_results.append(formatted_file)
    return formatted_results
