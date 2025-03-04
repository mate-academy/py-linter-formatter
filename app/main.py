def format_linter_error(error: dict) -> dict:
    return {
        key: error.get(val, 0 if key in ["line", "column"] else "")
        for key, val in [
            ("line", "line_number"),
            ("column", "column_number"),
            ("message", "text"),
            ("name", "code"),
        ]
    } | {"source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [
            {
                "line": error["line_number"],
                "column": error["column_number"],
                "message": error["text"],
                "name": error["code"],
                "source": "flake8",
            }
            for error in errors
        ],
        "path": file_path,
        "status": "failed" if errors else "passed",
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "path": path,
            "errors": [format_linter_error(err) for err in errors],
            "status": "failed" if errors else "passed",
        }
        for path, errors in linter_report.items()
    ]
