def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [format_linter_error(errors[line])
                       for line in range(len(errors))],
            "path": file_path, "status": "failed"}


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(keys, values)
            if linter_report[keys] != [] else
            {"errors": [], "path": keys, "status": "passed"}
            for keys, values in linter_report.items()]
