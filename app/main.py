def format_linter_error(error: dict) -> dict:
    return {["name", "message", "column", "line", "source"]
            [a]:
                [[error. get(i) for i in
                  ["code", "text", "column_number", "line_number"]]
                 + ["flake8"]][0][a] for a in range(5)}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [format_linter_error(error) for error in errors]} \
        | {"path": file_path} | \
        {"status": "failed" if len(errors) > 0 else "passed"}


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(b, linter_report[b])
            for b in linter_report]
