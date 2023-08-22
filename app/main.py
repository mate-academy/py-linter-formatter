def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "flake8"
         }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [{"line": error["line_number"],
                        "column": error["column_number"],
                       "message": error["text"], "name": error["code"],
                        "source": "flake8"} for error in errors],
            "path": file_path,
            "status": ("failed" if len(errors) > 0 else "passed")}


def format_linter_report(linter_report: dict) -> list:
    return [{"errors": [{"line": lin_err["line_number"],
                         "column": lin_err["column_number"],
                         "message": lin_err["text"],
                         "name": lin_err["code"],
                         "source": "flake8"
                         } for lin_err in lin_value],
             "path": lin_key,
             "status": ("failed" if len(lin_value) > 0 else "passed")}
            for lin_key, lin_value in linter_report.items()]
