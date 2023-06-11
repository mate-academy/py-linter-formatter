def format_linter_error(error: dict) -> dict:
    return {["name", "message", "column", "line", "source"]
            [a]:
                [[error. get(i) for i in
                  ["code", "text", "column_number", "line_number"]]
                 + ["flake8"]][0][a] for a in range(5)}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [{["name", "message", "column", "line", "source"][a]
                        : [[error. get(i) for i in
                            ["code", "text", "column_number", "line_number"]]
                           + ["flake8"]][0][a] for a
                        in range(5)} for error in errors]} \
        | {"path": file_path} | \
        {"status": "failed" if len(errors) > 0 else "passed"}


def format_linter_report(linter_report: dict) -> list:
    return [{"errors": [{["name", "message", "column", "line", "source"][a]
                         :[[error.get(i) for i in
                            ["code", "text", "column_number", "line_number"]]
                           + ["flake8"]][0][a] for a in range(5)}
                        for error in linter_report[b]]}
            | {"path": b}
            | {"status": ("failed" if len(linter_report[b]) > 0 else "passed")}
            for b in linter_report]
