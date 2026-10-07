def format_linter_error(error: dict) -> dict:
    return {
        **{
            "name" if key == "code" else
            "line" if key == "line_number" else
            "column" if key == "column_number" else
            "message": value
            for key, value in error.items()
            if key in ("code", "line_number", "column_number", "text")
        },
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed" if len(errors) > 0 else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(path, errors)
            for path, errors in linter_report.items()]
