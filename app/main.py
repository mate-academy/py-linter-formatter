def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"], "column": error["column_number"], "message": error["text"], "name": error["code"], "source": "flake8"}  # noqa: E501


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [format_linter_error(err) for err in errors], "path": file_path, "status": "failed" if errors else "passed"}  # noqa: E501


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(path, err) for path, err in linter_report.items()]  # noqa: E501
