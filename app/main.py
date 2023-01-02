def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [
            {"line": value for key, value in error.items()
             if key == "line_number"}
            | {"column": value for key, value in error.items()
               if key == "column_number"}
            | {"message": value for key, value in error.items()
               if key == "text"}
            | {"name": value for key, value in error.items()
               if key == "code"}
            | {"source": "flake8"} for error in errors
        ],
        "path": file_path,
        "status": ("passed" if len(errors) == 0 else "failed")
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {"errors": []}
        | {"path": name}
        | {"status": "passed"} if len(inside) == 0 else {
            "errors": [
                {"line": value for key, value in error.items()
                 if key == "line_number"}
                | {"column": value for key, value in error.items()
                   if key == "column_number"}
                | {"message": value for key, value in error.items()
                   if key == "text"}
                | {"name": value for key, value in error.items()
                   if key == "code"}
                | {"source": "flake8"} for error in inside
            ],
            "path": name,
            "status": "failed"
        } for name, inside in linter_report.items()
    ]
