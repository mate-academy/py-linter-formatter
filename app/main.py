def format_linter_error(error: dict) -> dict:
    return {
        it: [
            v for k, v in error.items()
            if k in ["code", "line_number", "column_number", "text"]][i]
        if it != "source" else "flake8"
        for i, it in enumerate(["name", "line", "column", "message", "source"])
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:

    return {
        "errors": [format_linter_error(err) for err in errors],
        "path": file_path,
        "status": "failed" if len(errors) else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(key, value)
        for key, value in linter_report.items()
    ]
