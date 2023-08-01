def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8",
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [
            format_linter_error(dict_error) for dict_error in errors
        ],
        "path": file_path,
        "status": "failed" if errors else "passed",
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(path_to_file, list_of_errors)
        for path_to_file, list_of_errors in linter_report.items()
    ]
