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
            "status": "failed"}


def format_linter_report(linter_report: dict) -> list:

    return [{"errors": [
        {"line": linter_report[path][path_in]["line_number"],
         "column": linter_report[path][path_in]["column_number"],
         "message": linter_report[path][path_in]["text"],
         "name": linter_report[path][path_in]["code"],
         "source": "flake8"} for path_in in range(len(linter_report[path]))],
        "path": f"{path}",
        "status": ("passed" if linter_report[path] == [] else "failed")}
        for path, error in linter_report.items()]
