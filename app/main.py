def format_linter_error(error: dict) -> dict:
    # Error type correction
    return {"line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "flake8"
            }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # Change error type by file
    return {"errors": [format_linter_error(error) for error in errors],
            "path": file_path,
            "status": "passed" if errors == [] else "failed"
            }


def format_linter_report(linter_report: dict) -> list:
    # Grouping files into a list
    return [format_single_linter_file(key, value)
            for key, value in linter_report.items()]
