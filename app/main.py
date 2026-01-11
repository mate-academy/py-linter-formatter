def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"], "column": error["column_number"], "message": error["text"],"name":error["code"], "source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors":[
            {
                "line": info["line_number"],
                "column": info["column_number"],
                "message": info["text"],
                "name": info["code"],
                "source": "flake8"
            }
            for info in errors
        ],
        "path": file_path,
        "status": "failed" if errors else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
        "errors":[
            {
                "line": info["line_number"],
                "column": info["column_number"],
                "message": info["text"],
                "name": info["code"],
                "source": "flake8"
            }
            for info in errors
        ] if errors else [],
        "path": name,
        "status": "failed" if errors else "passed"
        } for name, errors in linter_report.items()
    ]
