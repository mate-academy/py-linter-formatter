def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "fleak8"
            }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    status = "passed" if not errors else "failed"
    return {
        "errors": [
            {
                "line": error["line_number"],
                "column": error["column_number"],
                "message": error["text"],
                "name": error["code"],
                "source": "fleak8"
            } for error in errors
        ],
        "path": file_path,
        "status": status
    }


def format_linter_report(linter_report: dict) -> list:
    errors = []

    for path, error_list in linter_report.items():
        formatted_errors = []

        for error in error_list:
            formatted_error = {
                "line": error["line_number"],
                "column": error["column_number"],
                "message": error["text"],
                "name": error["code"],
                "source": "fleak8"
            }
            formatted_errors.append(formatted_error)

        status = "failed" if formatted_errors else "passed"

        errors.append({
            "errors": formatted_errors,
            "path": path,
            "status": status
        })

    return errors
