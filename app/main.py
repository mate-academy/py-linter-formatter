def format_linter_error(error: dict) -> dict:
    return {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code"),
        "source": "flake8",
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors":
            [{"line": error.get("line_number"),
              "column": error.get("column_number"),
              "message": error.get("text"),
              "name": error.get("code"),
              "source": "flake8"} for error in errors],
        "path": file_path,
        "status": "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": list(linter_report.items())[0][1],
            "path": list(linter_report.items())[0][0],
            "status": "passed",
        },
        *[
            {
                "errors": [
                    {
                        "line": e.get("line_number"),
                        "column": e.get("column_number"),
                        "message": e.get("text"),
                        "name": e.get("code"),
                        "source": "flake8",
                    }
                    for e in errors
                ],
                "path": path,
                "status": "failed",
            }
            for path, errors in list(linter_report.items())[1:]
        ]
    ]
