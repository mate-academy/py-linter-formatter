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
        # "errors": [format_linter_error(error) for error in errors],
        "errors": list(map(format_linter_error, errors)),
        "path": file_path,
        "status": "passed" if len(errors) == 0 else "failed",
    }


def format_linter_report(linter_report: dict) -> list:
    return list(
        map(
            lambda item: format_single_linter_file(item[0], item[1]),
            linter_report.items()
        )
    )
