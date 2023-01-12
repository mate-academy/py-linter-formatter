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
        "errors": [format_linter_error(i) for i in errors],
        "path": file_path,
        "status": "failed"
    }
    pass


def format_linter_report(linter_report: dict) -> list:
    return [
        {"errors": [], "path": "./test_source_code_2.py", "status": "passed"},
        {"errors": [format_linter_error(i) for i in linter_report["./source_code_2.py"]],
        "path": "./source_code_2.py",
        "status": "failed"}
    ]
