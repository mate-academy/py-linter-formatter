

clear_dict = {
    "line_number" : "line",
    "column_number" : "column",
    "text" : "message",
    "code" : "name",
    "source" : "source"
}


def format_linter_error(error: dict) -> dict:
    return {
        clear_dict.get(err_key) : "flake8"
        if err_key == "source" else error.get(err_key)
        for err_key in list(error.keys()) + ["source"]
        if err_key in clear_dict
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors" : [format_linter_error(error) for error in errors],
        "path" : file_path,
        "status" : "failed" if [format_linter_error(error)
                                for error in errors] else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(
            linter_report_key,
            linter_report.get(linter_report_key)
        )
        for linter_report_key in linter_report.keys()
    ]
