def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8",
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [
            {
                "line": errors_list["line_number"],
                "column": errors_list["column_number"],
                "message": errors_list["text"],
                "name": errors_list["code"],
                "source": "flake8",
            }
            for errors_list in errors
        ],
        "path": file_path,
        "status": "passed" if errors == [] else "failed",
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file_link, error_list)
        for file_link, error_list in linter_report.items()
    ]
