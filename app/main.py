def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    res_dict_2 = {}
    result = []

    for error in errors:
        result_1 = {
            "line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "flake8"
        }

        result.append(result_1)
        res_dict_2["errors"] = result
        res_dict_2["path"] = file_path

        if error:
            res_dict_2["status"] = "failed"
        else:
            res_dict_2["status"] = "passed"


    return res_dict_2


def format_linter_report(linter_report: dict) -> list:
    result_dict_3 = {}
    result_dict_4 = {}
    res = []
    result_list = []
    for key, value in linter_report.items():
        print(key)
        if value == []:
            result_dict_4["errors"] = []
            result_dict_4["path"] = key
            result_dict_4["status"] = "passed"
        else:
            for _ in value:
                dict_1 = {
                    "line": _["line_number"],
                    "column": _["column_number"],
                    "message": _["text"],
                    "name": _["code"],
                    "source": "flake8"
                }
                res.append(dict_1)
            result_dict_3["errors"] = res
            result_dict_3["path"] = key
            result_dict_3["status"] = "failed"
    result_list.append(result_dict_4)
    result_list.append(result_dict_3)
    return result_list
