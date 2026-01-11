def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line"],
        "column": error["column"],
        "message": error["message"],
        "code": error["code"],
        "formatted": f"Line {error['line']}, Col {error['column']}: {error['message']} ({error['code']})"
    }
    pass


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "file": file_path,
        "errors": [format_linter_error(err) for err in errors]
    }
    pass


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file, errors)
        for file, errors in linter_report.items()
        if errors  # skip files with no errors
    ]
    pass
