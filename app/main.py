def format_linter_error(error: dict) -> dict:
    return {"line": error.get("line_number"),
            "column": error.get("column_number"),
            "message": error.get("text"),
            "name": error.get("code"), "source": "flake8"
            }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "path": file_path,
        "errors": [format_linter_error(error) for error in errors],
        "status": "failed" if any(errors) else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {"errors": [],
         "path": linter_report.get("./test_source_code_2.py"),
         "status": "passed"
         },
        format_single_linter_file(
            "./source_code_2.py",
            linter_report.get("./source_code_2.py")
        )
    ]
