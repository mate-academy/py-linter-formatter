def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [format_linter_error(error) for error in errors]
            if errors else [],
            "path": file_path,
            "status": "passed" if not errors else "failed"}


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [format_linter_error(error) 
            for error in linter_report[file_name]],
            "path": file_name,
            "status": "failed" if linter_report[file_name] else "passed"
        }
        for file_name in linter_report.keys()
    ]
