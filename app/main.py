def format_linter_error(error: dict) -> dict:

    return {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"), "name": error.get("code"),
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors":
            [format_linter_error(listed) for listed in errors],
        "path": file_path,
        "status": ("failed" if
                   [format_linter_error(listed) for listed in errors]
                   != [] else "passed")
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(path, error)
        for (path, error) in linter_report.items()
    ]
