def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [{"line": errors[i]["line_number"],
                        "column": errors[i]["column_number"],
                        "message": errors[i]["text"],
                        "name": errors[i]["code"],
                        "source": "flake8"} for i in range(len(errors))],
            "path": file_path,
            "status": "failed" if len(errors) > 0 else "passed"}


def format_linter_report(linter_report: dict) -> list:
    return [{
        "errors":  [] if len(linter_report[key]) == 0 else[{
                    "line": i["line_number"],
                    "column": i["column_number"],
                    "message": i["text"],
                    "name": i["code"],
                    "sourse": "flake8"} for i in linter_report[key]],
        "path": key,
        "status": "passed" if len(linter_report[key]) == 0 else "failed"}
        for key in linter_report.keys()]
