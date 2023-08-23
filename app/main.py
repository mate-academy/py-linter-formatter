def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    list_in_dict = []
    for elem in errors:
        formatted_error = {
            "line": elem["line_number"],
            "column": elem["column_number"],
            "message": elem["text"],
            "name": elem["code"],
            "source": "flake8"
        }
        list_in_dict.append(formatted_error)

    status = "failed" if list_in_dict else "passed"

    return {
        "errors": list_in_dict,
        "path": file_path,
        "status": status
    }


def format_linter_report(linter_report: dict) -> list:
    formatted_reports = []
    for file_path, errors in linter_report.items():
        formatted_errors = []
        for elem in errors:
            formatted_error = {
                "line": elem.get("line_number"),
                "column": elem.get("column_number"),
                "message": elem.get("text"),
                "name": elem.get("code"),
                "source": "flake8"
            }
            formatted_errors.append(formatted_error)
        formatted_reports.append({
            "errors": formatted_errors,
            "path": file_path
        })
    for report in formatted_reports:
        if report["errors"]:
            report["status"] = "failed"
        else:
            report["status"] = "passed"

    return formatted_reports
