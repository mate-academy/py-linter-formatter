def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # result = {
    #     "errors": [],
    #     "path": file_path,
    #     "status": "passed"
    # }
    #
    # for error in errors:
    #     if error["filename"] == file_path:
    #         result["errors"].append(format_linter_error(error))
    #         result["status"] = "failed"
    #
    # return result

    return {
        "errors": [
            format_linter_error(error)
            for error in errors if error["filename"] == file_path
        ],
        "path": file_path,
        "status": "passed"
        if all(
            error["filename"] != file_path for error in errors
        ) else "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(key, value)
        for key, value in linter_report.items()
    ]
