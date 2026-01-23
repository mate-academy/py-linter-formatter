def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    formatted_errors = [
        {
            "line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "flake8"
        }
        for error in errors
    ]

    status = "failed" if errors else "passed"

    return {
        "errors": formatted_errors,
        "path": file_path,
        "status": status
    }


def format_linter_report(linter_report: dict) -> list:
    formatted_report = []

    for file_path, errors in linter_report.items():
        formatted_errors = [
            {
                "line": error["line_number"],
                "column": error["column_number"],
                "message": error["text"],
                "name": error["code"],
                "source": "flake8"
            }
            for error in errors
        ]

        status = "failed" if errors else "passed"

        formatted_report.append({
            "errors": formatted_errors,
            "path": file_path,
            "status": status
        })

    return formatted_report
