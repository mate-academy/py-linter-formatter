def format_linter_error(error: dict) -> dict:
    return {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code"),
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [format_linter_error(error) for error in errors],
            "path": file_path,
            "status": ("passed" if len(errors) == 0 else "failed")}


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file_path=file_path, errors=errors_list)
        for file_path, errors_list in linter_report.items()
    ]

