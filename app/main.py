def format_linter_error(error: dict) -> dict:
    # write your code here
    # pass
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"

    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {

        "errors": [format_linter_error(num) for num in errors],
        "path": file_path,
        "status": "failed" if len(errors) else "passed"


    }

    #     "errors": {
    #         "line": data["line_number"],
    #         "column": data["column_number"],
    #         "message": data["text"],
    #         "name": data["code"],
    #         "source": "flake8"
    #         for data in errors]
    # },


def format_linter_report(linter_report: dict) -> list:
    # write your code here
    pass
