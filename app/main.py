def format_linter_error(error: dict) -> dict:
    return {
        "line": error.get("line"),
        "column": error.get("column"),
        "message": error.get("message"),
        "code": error.get("code")
    }

def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "file": file_path,
        "errors": [format_linter_error(err) for err in errors]
    }

def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file_path, errors)
        for file_path, errors in linter_report.items()
    ]
