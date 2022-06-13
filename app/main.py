def format_linter_error(error: dict) -> dict:
    # white your code here
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8",
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(er) for er in errors],
        "path": file_path,
        "status": "passed" if len(errors) == 0 else "failed"
    }

def format_linter_report(linter_report: dict) -> list:

    return [format_single_linter_file(file_name, linter_report[file_name]) for file_name in linter_report]
