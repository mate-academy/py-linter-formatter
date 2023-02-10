def format_linter_error(error: dict) -> dict:
    return {"line": error.get("line_number"),
            "column": error.get("column_number"),
            "message": error.get("text"),
            "name": error.get("code"),
            "source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors":
            [{"line": error_dict["line_number"],
              "column": error_dict["column_number"],
              "message": error_dict["text"],
              "name": error_dict["code"],
              "source": "flake8"} for error_dict in errors],
        "path": file_path,
        "status": "failed" if len(errors) > 0 else "passed"}


def format_linter_report(linter_report: dict) -> list:
    return [{"errors": linter_report.get("./test_source_code_2.py"),
             "path": [k for k in linter_report.keys()][0],
             "status": "passed"},
            {"errors": [{"line": error_dict["line_number"],
                         "column": error_dict["column_number"],
                         "message": error_dict["text"],
                         "name": error_dict["code"],
                         "source": "flake8"} for error_dict in linter_report.get("./source_code_2.py")],
             "path": "./source_code_2.py",
             "status": "failed"}]
