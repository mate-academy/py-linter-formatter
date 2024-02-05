def format_linter_error(error: dict) -> dict:
    return {
        **{
            k: error[v]
            for k, v in {
                "line": "line_number",
                "column": "column_number",
                "message": "text",
                "name": "code"
            }.items()
        },
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(error=error) for error in errors],
        "path": file_path,
        "status":
            "passed"
            if len([format_linter_error(error=error) for error in errors]) == 0
            else "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file_path=path, errors=errors)
        for path, errors in linter_report.items()
    ]
