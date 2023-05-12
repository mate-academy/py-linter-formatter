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
        "errors":
            [
                {
                    "line": err["line_number"],
                    "column": err["column_number"],
                    "message": err["text"],
                    "name": err["code"],
                    "source": "flake8"}
                for err in errors],
        "path": file_path,
        "status": "failed"
        if errors else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors":
                [
                    {
                        "line": item["line_number"],
                        "column": item["column_number"],
                        "message": item["text"],
                        "name": item["code"],
                        "source": "flake8"}
                    for item in linter_report[corr]
                    if item["filename"] in corr and item["text"] and item["code"]],
            "path": corr,
            "status": "failed"
            if any(item["text"] and item["code"]
                   for item in linter_report[corr])
            else "passed"

        }
        for corr in linter_report
    ]
