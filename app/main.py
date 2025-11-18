def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8",
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [{"line": v["line_number"],
                        "column": v["column_number"],
                        "message": v["text"],
                        "name": v["code"],
                        "source": "flake8"}for v in errors],
            "path": file_path, "status": "failed" if errors else "passed", }


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(k, v) for k, v in linter_report.items()]
