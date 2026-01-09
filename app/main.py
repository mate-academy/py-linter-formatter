def format_linter_error(error: dict) -> dict:
    return {"message": error.get("text",""), "name": error.get("code",""), "line": error.get("line_number", 0), "column": error.get("column_number", 0), "source":"flake8"}
    pass


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors":[format_linter_error(error) for error in errors], "path": file_path, "status": "failed" if errors else "passed"}
    pass


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(file_path=path, errors=errs) for path, errs in linter_report.items()]
