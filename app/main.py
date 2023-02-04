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
        "errors": [{
            "line": i["line_number"],
            "column": i["column_number"],
            "message": i["text"],
            "name": i["code"],
            "source": "flake8"
        }
            for i in errors
        ],
        "path": file_path,
        "status": "failed" if len(errors) > 0 else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [{
        "errors": [{
            "line": a["line_number"],
            "column": a["column_number"],
            "message": a["text"],
            "name": a["code"],
            "source": "flake8"
        }
            for a in linter_report[i]],
        "path": i,
        "status": "passed"
        if linter_report[i] == [] else "failed"}for i in linter_report]
