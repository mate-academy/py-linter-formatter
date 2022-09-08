def format_linter_error(error: dict) -> dict:
    # white your code here
    return {"line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "flake8",
            }
    pass


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # white your code here
    return {"errors": [format_linter_error(er) for er in errors],
            "path": file_path,
            "status": "failed" if len([format_linter_error(er)
                                       for er in errors]) else "passed"
            }
    pass


def format_linter_report(linter_report: dict) -> list:
    # white your code here
    return [format_single_linter_file(file_path_error, error_description)
            for file_path_error, error_description in linter_report.items()]
    pass
