def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "flake8"} \
        if len(error) > 0 else {}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [format_linter_error(dic) for dic in errors],
            "path": file_path,
            "status": "failed"
            if len(errors) > 0 else "passed"}


def format_linter_report(linter_report: dict) -> list:
    return [{"errors": [format_linter_error(dic)
                        for dic in linter_report[index]],
             "path": index, "status": "failed" if len(linter_report[index]) > 0
            else "passed"} for index in linter_report]
