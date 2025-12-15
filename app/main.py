def format_linter_error(single_error: dict) -> dict:
    return {
        "line": single_error.get("line_number", 0),
        "column": single_error.get("column_number", 0),
        "message": single_error.get("text", "No message"),
        "name": single_error.get("code", "E501"),
        "source": single_error.get("source", "flake8"),
    }


def format_single_linter_file(file_path: str, file_errors: list) -> dict:
    return {
        "errors":
            [format_linter_error(file_error) for file_error in file_errors],
        "path": file_path,
        "status": "failed" if file_errors else "passed"
    }


def format_linter_report(full_report: dict) -> list:
    return [
        format_single_linter_file(file_path, path_errors)
        for file_path, path_errors in full_report.items()
    ]
