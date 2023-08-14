def format_linter_error(error: dict) -> dict:
    # formats a single error:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"  # add key "source" : value = "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    #  formats all errors
    return {
        "errors": [
            format_linter_error(err) for err in errors
        ],
        "path": file_path,
        "status": "passed" if errors == [] else "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    # formats all errors for all report files:
    return [
        format_single_linter_file(linter[0], linter[1])
        for linter in list(linter_report.items())
    ]
