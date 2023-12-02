def format_linter_error(error: dict) -> dict:
    if len(error) == 0:
        return {}
    formatted_error = {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }
    return formatted_error


def format_single_linter_file(file_path: str, errors: list) -> dict:
    errors_list = []
    status = "failed" if len(errors) != 0 else "passed"
    if status == "failed":
        for error in errors:
            formatted_error = {
                "line": error["line_number"],
                "column": error["column_number"],
                "message": error["text"],
                "name": error["code"],
                "source": "flake8"
            }
            errors_list.append(formatted_error)
    result_dict = {"errors": errors_list,
                   "path": file_path,
                   "status": status}
    return result_dict


def format_linter_report(linter_report: dict) -> list:
    result = []
    file_names = list(linter_report.keys())
    status_list = []
    for file_name in file_names:
        status_list.append("passed" if len(linter_report[file_name]) == 0
                           else "failed")
    for value in range(len(status_list)):
        sub_list = []
        if status_list[value] == "failed":
            errors_list = linter_report[file_names[value]]
            for error in errors_list:
                formatted_error = {
                    "line": error["line_number"],
                    "column": error["column_number"],
                    "message": error["text"],
                    "name": error["code"],
                    "source": "flake8"
                }
                sub_list.append(formatted_error)

        sub_dict = {"errors": sub_list,
                    "path": file_names[value],
                    "status": status_list[value]}

        result.append(sub_dict)

    return result


