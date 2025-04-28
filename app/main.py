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
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed" if errors != [] else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    # for i in linter_report:
    #     print(linter_report[i])
    return [
        format_single_linter_file(one_file, linter_report[one_file])
        for one_file in linter_report
    ]
