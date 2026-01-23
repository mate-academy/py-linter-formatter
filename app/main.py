
def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


# format_linter_error(error=error)


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
    "errors":
        [
            format_linter_error(error=errors[0]),
            format_linter_error(error=errors[1])
        ],
    "path": file_path,
    "status": "failed"
}


# format_single = format_single_linter_file(file_path="./source_code_2.py", errors=errors)


def format_linter_report(linter_report: dict) -> list:
    return [
    {
        "errors": report_file["./test_source_code_2.py"],
        "path": "./test_source_code_2.py",
        "status": "failed"
    }, format_single_linter_file(file_path="./source_code_2.py", errors=errors)
    ]


# format_linter_report(linter_report=report_file)