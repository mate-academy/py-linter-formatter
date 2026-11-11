def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],           # the base dictionary format we will be using - DRY
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8",
    }

def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors":
            [
                format_linter_error(error)      # list comprehension
                for error in errors
            ],
        "path": file_path,
        "status": "failed" if errors else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file_path, file_errors)   # list comprehension
        for file_path, file_errors in linter_report.items() # .items() converts dictionary into a view of tuples that file_path, file_errors unpack
    ]
