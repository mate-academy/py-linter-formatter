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
            {
                "line": n["line_number"],
                "column": n["column_number"],
                "message": n["text"],
                "name": n["code"],
                "source": "flake8",
            }
            for n in errors
        ],
        "path": file_path,
        "status": "failed",
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [
                {
                    "line": val["line_number"],
                    "column": val["column_number"],
                    "message": val["text"],
                    "name": val["code"],
                    "source": "flake8",
                }
                for val in linter_report[err]
            ],
            "path": err,
            "status": ("passed" if len(linter_report[err]) == 0 else "failed"),
        }
        for err in linter_report
    ]
