def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8",
    }

def format_single_linter_file(file_path: str, errors: list) -> dict:
    formatted_errors = []
    for error in errors:
        formatted_errors.append(format_linter_error(error))
    if error != {}:
        status = "failed"
    else:
        status = "passed"
    return {"errors": formatted_errors, "path": errors["filename"], "status": status}


def format_linter_report(linter_report: dict) -> list:
    result = {}
    formated_errors = []
    for key, value in linter_report.items():
        if not linter_report[key]:
            result.update({"errors": [], "path": key, "status": "passed"})
        if linter_report[key]:
            for char in value:
                formatted_char = format_linter_error(char)
                formated_errors.append(formatted_char)
            result.update({"errors": formated_errors, "path": key, "status": "failed"})
    return result

