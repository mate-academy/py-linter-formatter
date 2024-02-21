def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"] if "line_number" in error else None,
        "column": error["column_number"] if "column_number" in error else None,
        "message": error["text"] if "text" in error else None,
        "name": error["code"] if "code" in error else None,
        "source": "flake8"
    }
    pass


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors":
            [
                {
                    "line": error["line_number"]
                    if "line_number" in error else None,
                    "column": error["column_number"]
                    if "column_number" in error else None,
                    "message": error["text"]
                    if "text" in error else None,
                    "name": error["code"]
                    if "code" in error else None,
                    "source": "flake8"
                }
                for error in errors
            ],
        "path": file_path,
        "status": "failed" if errors != 0 else "passed"
    }
    pass


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [],
            "path": path,
            "status": "passed"
        }
        if errors == []
        else {
            "errors":
            [
                {
                    "line": error["line_number"]
                    if "line_number" in error else None,
                    "column": error["column_number"]
                    if "column_number" in error else None,
                    "message": error["text"]
                    if "text" in error else None,
                    "name": error["code"]
                    if "code" in error else None,
                    "source": "flake8"
                }
                for error in errors
            ],
            "path": path,
            "status": "failed"
        }
        for path, errors in linter_report.items()
    ]
    pass
