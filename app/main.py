

clear_dict = {
    "line_number" : "line",
    "column_number" : "column",
    "text" : "message",
    "code" : "name",
    "source" : "source"
}


def gets_errors(errors: list, file_path: str) -> list:
    error = [
        format_linter_error(error)
        for error in errors
        if error.get("filename") == file_path
    ]

    satus = "failed" if error else "passed"
    return [error, satus]


def format_linter_error(error: dict) -> dict:
    return {
        clear_dict.get(err_key) : "flake8"
        if err_key == "source" else error.get(err_key)
        for err_key in list(error.keys()) + ["source"]
        if err_key in clear_dict
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors" : gets_errors(file_path=file_path, errors=errors)[0],
        "path" : file_path,
        "status" : gets_errors(file_path=file_path, errors=errors)[1]
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(
            linter_report_key,
            linter_report.get(linter_report_key)
        )
        for linter_report_key in linter_report.keys()
    ]
