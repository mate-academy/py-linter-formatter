def format_linter_error(error: dict) -> dict:
    return {"line": error["line"], "error": error["message"]}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {file_path: [
        format_linter_error(error) for error in errors]} \
        if errors else {file_path: []}


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file, errors)
        for file, errors in linter_report.items()
    ]
