def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"], "column": error["column_number"], "message": error["text"], "name": error["code"], "source": "flake8"}
# {
#     "line": 18,
#     "column": 80,
#     "message": "line too long (99 > 79 characters)",
#     "name": "E501",
#     "source": "flake8"
# }

def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors":[format_linter_error(error=error) for error in errors], "path": file_path, "status": "failed" if len(errors) != 0 else "passed"}


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(path, errors_for_that_path) for path, errors_for_that_path in linter_report.items()]


