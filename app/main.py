def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [
            {
                "line": errors[0]["line_number"],
                "column": errors[0]["column_number"],
                "message": errors[0]["text"],
                "name": errors[0]["code"],
                "source": "flake8"
            },
            {
                "line": errors[1]["line_number"],
                "column": errors[1]["column_number"],
                "message": errors[1]["text"],
                "name": errors[1]["code"],
                "source": "flake8"
            }
        ],
        "path": file_path,
        "status": "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [
                {
                    "line": item.get("line_number", 0),
                    "column": item.get("column_number", 0),
                    "message": item.get("text", ""),
                    "name": item.get("code", ""),
                    "source": "flake8"
                }
                for item in linter_report.get(file, [])
            ],
            "path": file,
            "status": "failed" if linter_report.get(file) else "passed"
        }
        for file in linter_report.keys()
    ]
