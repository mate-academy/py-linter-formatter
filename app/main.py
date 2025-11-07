def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line"],
        "symbol": error["symbol"],
        "message": error["message"],
        "code": error["code"],
    }


def format_single_linter_file(file_path: str, errors: list[dict]) -> dict:
    return {
        "file": file_path,
        "errors": [format_linter_error(error) for error in errors],
    }


def format_linter_report(linter_report: dict[str, list[dict]]) -> list[dict]:
    return [
        format_single_linter_file(file_path, errors)
        for file_path, errors in linter_report.items()
    ]
