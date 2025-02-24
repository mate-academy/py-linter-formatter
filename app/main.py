def format_linter_error(error: dict) -> dict:

    return ({
        {"line_number": "line", "column_number": "column", "text": "message", "code": "name"}.get(
            key): value
        for key, value in error.items()
        if key in ["line_number", "column_number", "text", "code"]}
            | {"source": "flake8"})


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors":
        [
        {
        {"line_number": "line", "column_number": "column", "text": "message", "code": "name"}.get(key): value
        for key, value in error.items()
        if key in ["line_number", "column_number", "text", "code"]} | {"source": "flake8"}
        for error in errors
        ],
        "path": file_path,
        "status": "failed" if errors else "passed"
        }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [
                {
                    {"line_number": "line", "column_number": "column", "text": "message", "code": "name"}.get(
                        key): value
                    for key, value in error.items()
                    if key in ["line_number", "column_number", "text", "code"]
                } | {"source": "flake8"}
                for error in errors
            ],
            "path": file_path,
            "status": "failed" if errors else "passed"
        }
        for file_path, errors in linter_report.items()
        ]
