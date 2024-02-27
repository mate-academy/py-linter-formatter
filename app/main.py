def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(erroy) for erroy in errors],
        "path": file_path,
        "status": "failed" if len(errors) > 0 else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [format_linter_error(erroy)
                       for erroy
                       in linter_report[error_report]
                       ],
            "path": error_report,
            "status": "failed"
                      if len(linter_report[error_report]) > 0
                      else "passed"
        }
        for i, error_report in enumerate(linter_report)
    ]
