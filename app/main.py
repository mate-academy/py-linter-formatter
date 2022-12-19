def format_linter_error(error: dict) -> dict:
    # reformat single error, replace  keys with new keys
    # with the same values
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:

    # create the dictionary with 3 keys,
    # key "errors" : value (list of errors)
    return {
        "errors":
            [
                # call function every time to collect errors
                format_linter_error(error) for error in errors
            ],
        "path": file_path,
        "status": "failed" if errors else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    # take function format_single_linter_file
    # with its parameters, and create
    # new dictionary of arguments from the last function
    return [
        format_single_linter_file(file_path, errors)
        for file_path, errors in linter_report.items()
    ]
