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
        "path": file_path,
        "errors": [format_linter_error(err) for err in errors],
        "status": "failed" if errors else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(path, errs) for path, errs in linter_report.items()]

error = {"code": "E501", "line_number": 18, "column_number": 80, "text": "line too long", "physical_line": "..."}
print(format_linter_error(error))
# → {"line": 18, "column": 80, "message": "line too long", "name": "E501", "source": "flake8"}