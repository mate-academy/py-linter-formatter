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
        "errors": [
            {
                "line": error["line_number"],
                "column": error["column_number"],
                "message": error["text"],
                "name": error["code"],
                "source": "flake8"
            }
            for error in errors
        ],

        "path": file_path,
        "status": "passed"
        if not any(err["filename"] == file_path for err in errors) else
        "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [{
        "errors": [
            {
                "line": error["line_number"],
                "column": error["column_number"],
                "message": error["text"],
                "name": error["code"],
                "source": "flake8"
            }
            for error in linter_report[file_path]
        ],
        "path": file_path,
        "status": "passed" if not linter_report[file_path] else "failed"
    } for file_path in linter_report]
