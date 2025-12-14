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
            format_linter_error(data_error)
            for data_error in errors
            if data_error["filename"] == file_path
        ],
        "path": file_path,
        "status": "failed" if any(errors) else "passed",
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(road_to_file, data_error)
        for road_to_file, data_error in linter_report.items()
    ]
