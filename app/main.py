def format_linter_error(error: dict) -> dict:
    return {
        {
            "code": "name",
            "text": "message",
            "line_number": "line",
            "column_number": "column",
            "filename": "source"
        }[signature]: ("flake8" if signature == "filename" else sense)
        for signature, sense in error.items()
        if signature != "physical_line"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [format_linter_error(error) for error in errors],
            "path": file_path,
            "status": "failed" if errors else "passed"}


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(signature, linter_report[signature])
            for signature in linter_report]
