def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8",
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "path": file_path,
        "status": "failed" if errors else "passed",
        "errors": [
            format_linter_error(e)
            for e in sorted(errors, key=lambda er: (er["line_number"], er["column_number"]))
        ],
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(path, errs)
        for path, errs in sorted(linter_report.items(), key=lambda it: it[0])
    ]
