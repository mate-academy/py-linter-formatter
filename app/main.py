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
        "errors":
            [
                {
                "line": error["line_number"],
                "column": error["column_number"],
                "message": error["text"],
                "name": error["text"],
                "source": "flake8"
                }
                for error in errors
            ],
        "path": file_path,
        "status": "passed" if "errors" == [] else "failed"
            }


def format_linter_report(linter_report: dict) -> list:
    return [
        {"errors":
            [
                {
                "line": error["line_number"],
                "column": error["column_number"],
                "message": error["text"],
                "name": error["text"],
                "source": "flake8"
                }
                for error in errors
            ],
        "path": linter_report[i],
        "status": "passed" if "errors" == [] else "failed"
        }
        for i, errors in enumerate(linter_report)
    ]
