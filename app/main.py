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
        "errors": [{
            "line": every["line_number"],
            "column": every["column_number"],
            "message": every["text"],
            "name": every["code"],
            "source": "flake8"
        } for every in errors if every["filename"] == file_path],
        "path": file_path,
        "status": "failed" if len(errors) > 0 else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {"errors": [{
            "line": linter_report[file_error][key_error]["line_number"],
            "column": linter_report[file_error][key_error]["column_number"],
            "message": linter_report[file_error][key_error]["text"],
            "name": linter_report[file_error][key_error]["code"],
            "source": "flake8"}
            for key_error, key in enumerate(linter_report[file_error])],
            "path": file_error,
            "status": "passed"
            if len(linter_report[file_error]) == 0 else "failed"}
        for file_error in linter_report
    ]
