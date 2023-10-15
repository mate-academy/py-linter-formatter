def format_linter_error(error: dict) -> dict:
    return {
        {
            "code": "name",
            "text": "message",
            "line_number": "line",
            "column_number": "column",
            "filename": "source"
        }[key]: ("flake8" if key == "filename" else val)
        for (key, val) in error.items()
        if key != "physical_line"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [format_linter_error(error) for error in errors],
            "path": file_path,
            "status": "passed" if errors == [] else "failed"}


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(key, linter_report[key])
            for (key, item) in linter_report.items()
            ]
