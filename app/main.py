def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "flake8"
            }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [{"line": errors[line]["line_number"],
                        "column": errors[line]["column_number"],
                        "message": errors[line]["text"],
                        "name": errors[line]["code"],
                        "source": "flake8"
                        } for line in range(len(errors))],
            "path": file_path, "status": "failed"}


def format_linter_report(linter_report: dict) -> list:
    return [{"errors": [{"line": value["line_number"],
                         "column": value["column_number"],
                         "message": value["text"],
                         "name": value["code"],
                         "source": "flake8"
                         } for value in values],
            "path": keys, "status": "failed"}
            if linter_report[keys] != [] else
            {"errors": [], "path": keys, "status": "passed"}
            for keys, values in linter_report.items()]
