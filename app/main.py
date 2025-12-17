def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"], "column": error["column_number"], "message": error["text"], "name": error["code"], "source": "flake8"}

def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [[] if len(errors) == 0 else format_linter_error(errors[i]) for i in range(len(errors))], "path": file_path, "status": "passed" if errors == [] else "failed"}

def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(list(linter_report.keys())[ind], list(linter_report.values())[ind]) for ind in range(len(linter_report))]