def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "flake8"
            }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    status = "passed" if not errors else "failed"
    formatted_errors = [format_linter_error(error) for error in errors]
    return {
        "errors": formatted_errors,
        "path": file_path,
        "status": status
    }


def format_linter_report(linter_report: dict) -> list:
    formatted_report = []
    for path, errors in linter_report.items():
        formatted_report.append(format_single_linter_file(file_path=path, errors=errors))
        return formatted_report
