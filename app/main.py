def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [
        {"line": errors[i]["line_number"],
         "column": errors[i]["column_number"],
         "message": errors[i]["text"],
         "name": errors[i]["code"],
         "source": "flake8"}
        for i in range(len(errors))],
        "path": str(file_path),
        "status": "failed"}


def format_linter_report(linter_report: dict) -> list:
    return [{"errors": [
        {"line": v[i]["line_number"],
         "column": v[i]["column_number"],
         "message": v[i]["text"],
         "name": v[i]["code"],
         "source": "flake8"}
        for i in range(len(v))], "path": k, "status": "failed"} if len(v) != 0
        else {"errors": v, "path": k, "status": "passed"}
        for k, v in linter_report.items()]
