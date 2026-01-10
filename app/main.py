def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"], "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors":
        [format_linter_error(error) for error in errors]
        if errors != [] else [], "status": "failed" if errors != []
        else "passed", "path": file_path
    }


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(file_path=key_report,
            errors=linter_report[key_report]) for key_report in linter_report]
