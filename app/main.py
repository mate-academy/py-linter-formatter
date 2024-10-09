def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line"],
        "message": error["message"],
        "severity": error["severity"]
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    formatted_errors = [format_linter_error(error) for error in errors]
    return {file_path: formatted_errors}


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(file_path, errors)
            for file_path, errors in linter_report.items()]
