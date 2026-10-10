def format_linter_error(error: dict) -> dict:
    return {
        {
            "line_number": "line",
            "column_number": "column",
            "text": "message",
            "code": "name",
            "source": "source",
        }[k]: v
        for k, v in list(error.items()) + [("source", "flake8")]
        if k in ["line_number", "column_number", "text", "code", "source"]
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [
            format_linter_error(error)
            for error in errors
        ],
        "path": file_path,
        "status": "failed" if errors else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file_path, errors)
        for file_path, errors in linter_report.items()
    ]
