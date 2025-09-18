def format_linter_error(error: dict) -> dict:
    return {
        "line": (
            error.get("line")
            or error.get("line_number")
            or error.get("lineNumber")
        ),
        "column": (
            error.get("column")
            or error.get("column_number")
            or error.get("columnNumber")
            or error.get("col")
        ),
        "name": (
            error.get("name")
            or error.get("code")
            or error.get("error")
        ),
        "message": (
            error.get("message")
            or error.get("text")
            or error.get("description")
        ),
        "source": error.get("source") or "flake8",
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "path": file_path,
        "status": (
            "failed"
            if (errs := [format_linter_error(e) for e in errors])
            else "passed"
        ),
        "errors": errs,
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(path, errs)
        for path, errs in linter_report.items()
    ]
