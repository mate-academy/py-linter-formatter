def format_linter_error(error: dict) -> dict:
    return {["name", "message", "column", "line", "source"][i]
            : error[["code", "text", "column_number", "line_number"][i]]
            for i in range(4)} | {"source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed" if len(errors) > 0 else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(error[0], error[1])
            for error in linter_report.items()]
