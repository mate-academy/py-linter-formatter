error_vars = {"line": "line_number",
              "column": "column_number",
              "message": "text",
              "name": "code",
              "source": "flake8"}


def format_linter_error(error: dict) -> dict:
    return {k: (error[v] if v in error.keys() else v)
            for k, v in error_vars.items()}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [format_linter_error(error) for error in errors],
            "path": file_path,
            "status": "failed" if errors else "passed"}


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(file_path=path,
                                      errors=linter_report[path])
            for path in linter_report.keys()]
