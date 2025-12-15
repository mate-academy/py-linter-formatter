def format_linter_error(error: dict) -> dict:
    return {"line": error.get("line_number"),
            "column": error.get("column_number"),
            "message": error.get("text"),
            "name": error.get("code"),
            "source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [format_linter_error(error) for error in errors],
            "path": file_path,
            "status": ("passed" if errors == [] else "failed")}


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(report[0], report[1])
            for report in linter_report.items()]
