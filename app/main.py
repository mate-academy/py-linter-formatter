def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error.get("text", "Error message not available"),
        "name": error.get("code", "Code not available"),
        "source": error.get("source", "flake8"),
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "path": file_path,
        "errors": [format_linter_error(error) for error in errors],
        "status": "passed" if not errors else "failed",
    }




def format_linter_report(linter_report: dict) -> list:
    return [{
        "path": path,
        "errors": [format_linter_error(error) for error in errors],
        "status": "passed" if not errors else "failed"}

        for path, errors in linter_report.items()
    ]
