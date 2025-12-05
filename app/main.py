def format_linter_error(error: dict) -> dict:
    return {
        "line": ...,
        "column": ...,
        "message": ...,
        "name": ...,
        "source": "flake8",
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [...],
        "path": file_path,
        "status": ...,
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        ...
    ]


