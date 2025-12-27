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
            {"line": error["line_number"],
             "column": error["column_number"],
             "message": error["text"],
             "name": error["code"],
             "source": "flake8"
             } for error in errors
        ],
        "path": file_path, "status": "failed" if len(errors) > 0 else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [{
        "path" : path,
        "status" : "failed" if len(error_list) > 0 else "passed",
            "errors": [{
                "line" : error["line_number"],
                "column" : error["column_number"],
                "message" : error["text"],
                "name" : error["code"],
                "source": "flake8"
            } for error in error_list]
            }for path, error_list in linter_report]
