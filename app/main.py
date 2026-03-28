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
        "status": "Failed" if errors != [] else "Passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file
        (
            i, [k for k in linter_report[i]]
        ) for i in linter_report
    ]
