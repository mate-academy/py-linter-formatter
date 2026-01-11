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
        "path": file_path,
        "errors": [
            {
                "line": e["line_number"],
                "column": e["column_number"],
                "message": e["text"],
                "name": e["code"],
                "source": "flake8",
            }
            for e in errors
        ],
        "status": "passed" if not errors else "failed",
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "path": f,
            "errors": [
                {
                    "line": e["line_number"],
                    "column": e["column_number"],
                    "message": e["text"],
                    "name": e["code"],
                    "source": "flake8",
                }
                for e in errs
            ],
            "status": "passed" if not errs else "failed",
        }
        for f, errs in linter_report.items()
    ]
