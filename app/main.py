def format_linter_error(error: dict) -> dict:
    return {
            key: value for (key, value) in
            zip(["line", "column", "message", "name", "source"],
            [error["line_number"], error["column_number"], error["text"], error["code"], "flake8"])
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(errors[i]) for i in range(len(errors))],
        "path": file_path,
        "status": "passed" if len(errors) == 0 else "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(test, error) for test, error in linter_report.items()]
