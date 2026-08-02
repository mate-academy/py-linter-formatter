def format_linter_error(error: dict) -> dict:
    # Transform one error into the required dictionary
    return {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code"),
        "source": "flake8"
    }


def format_single_linter_file(
        file_path: str,
        errors: list) -> dict[str, list[dict] | str]:
    # Format one file with all errors: errors, path, status
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "passed" if not errors else "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    # # Format all files in the linter report
    return [
        format_single_linter_file(file_path, errors)
        for file_path, errors in linter_report.items()
    ]
