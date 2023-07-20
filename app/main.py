def format_linter_report(linter_report: dict) -> list:
    return [
        {"errors":
             [
                 {"line": error["line_number"],
                  "column": error["column_number"],
                  "message": error["text"],
                  "name": error["code"],
                  "source": "flake8"} for error in errors],

            "path": path,
            "status": "failed" if errors else "passed"}
        for path, errors in linter_report.items()
    ]
