def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # bledy = []
    #
    # for er in errors:
    #     bledy.append(format_linter_error(er))
    #
    # stat = "passed" if not bledy else "failed"
    # rest = {
    #     "errors": bledy,
    #     "path": file_path,
    #     "status": stat
    # }
    return {
        "errors": [format_linter_error(er) for er in errors],
        "path": file_path,
        "status": "passed" if not errors else "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    # rest = []
    # for k, v in linter_report.items():
    #     rest.append(format_single_linter_file(k, v))

    return [
        format_single_linter_file(keys, values)
        for keys, values in linter_report.items()
    ]
