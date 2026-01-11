def format_linter_error(error: dict) -> dict:
    return ({("line" if key == "line_number"
             else "column" if key == "column_number"
             else "message" if key == "text"
             else "name" if key == "code"
             else key): value
            for key, value in error.items()
            if key in ["line_number", "column_number", "text", "code"]}
            | {"source": "flake8"})


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return ({"errors": [format_linter_error(error) for error in errors]}
            | {"path": file_path}
            | {"status": "failed" if len(errors) > 0 else "passed"})


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(key, value)
            for key, value in linter_report.items()]
