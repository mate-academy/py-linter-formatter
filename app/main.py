def format_single_linter_file_2(file_path: str, errors: list) -> dict:
    res_dict_2 = {}
    result = []

    for error in errors:
        formatted_error = {
            "line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "flake8"
        }

        result.append(formatted_error)

        res_dict_2["errors"] = result
        res_dict_2["path"] = error["filename"]

    if errors == []:
        res_dict_2["status"] = "passed"
    else:
        res_dict_2["status"] = "failed"
    return res_dict_2


def format_linter_report_2(linter_report: dict) -> list:
    result_list = []
    for key, value in linter_report.items():
        if value == []:
            result_dict = {
                "errors": [],
                "path": key,
                "status": "passed"
            }
        else:
            error = []
            for values in value:
                formatted_error = {
                    "line": values["line_number"],
                    "column": values["column_number"],
                    "message": values["text"],
                    "name": values["code"],
                    "source": "flake8"
                }
                error.append(formatted_error)
            result_dict = {
                "errors": error,
                "path": key,
                "status": "failed"
            }
        result_list.append(result_dict)
    return result_list


def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return format_single_linter_file_2(file_path, errors)


def format_linter_report(linter_report: dict) -> list:
    return format_linter_report_2(linter_report)
