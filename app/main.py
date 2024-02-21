def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        key: (
            [format_linter_error(error) for error in errors]
            if key == "errors" else
            file_path if key == "path" else
            "failed" if errors else
            "passed"
        )
        for key in ["errors", "path", "status"]
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(path, error)
        for path, error in linter_report.items()
    ]
