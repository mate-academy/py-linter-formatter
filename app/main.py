def format_linter_error(error: dict) -> dict:
    return {"line": error['line_number'],
            "column": error['column_number'],
            "message": error['text'],
            "name": error['code'],
            "source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [format_linter_error(err) for err in errors],
            "path": f"{file_path}",
            "status": "passed" if len(errors) < 1 else "failed"}


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(ls, linter_report[ls])
            for ls in linter_report]
