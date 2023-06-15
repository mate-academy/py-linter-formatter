def format_linter_error(error: dict) -> dict:
    return {
        error_detail_name: (
            error["line_number"] if error_detail_name == "line" else
            error["column_number"] if error_detail_name == "column" else
            error["text"] if error_detail_name == "message" else
            error["code"] if error_detail_name == "name" else "flake8"
        )
        for error_detail_name in [
            "line", "column", "message", "name", "source"
        ]
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [format_linter_error(error) for error in errors],
            "path": file_path,
            "status": "failed" if errors != [] else "passed"}


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(
            file_path=file_path,
            errors=error)
        for file_path, error in linter_report.items()
    ]
