def format_linter_error(error: dict) -> dict:
    res_dict = {}
    fin_res_dict = {"errors": []}
    keys_error = list(error.keys())

    for i in keys_error:
        for j in range(len(error[i])):
            if True:
                res_dict["line"] = error[i][j]["line_number"]
                res_dict["column"] = error[i][j]["column_number"]
                res_dict["message"] = error[i][j]["text"]
                res_dict["name"] = error[i][j]["code"]
                res_dict["source"] = "flake8"

            fin_res_dict["errors"].append(res_dict)
            res_dict = {}
    return fin_res_dict


def format_single_linter_file(file_path: str, errors: list) -> dict:



def format_linter_report(linter_report: dict) -> list:
    # white your code here
    pass


errors_ = {
    "./test_source_code_2.py": [],
    "./source_code_2.py": [
        {
            "code": "E501",
            "filename": "./source_code_2.py",
            "line_number": 18,
            "column_number": 80,
            "text": "line too long (99 > 79 characters)",
            "physical_line": '    return f"I like to filter, rounding, doubling, '
            "store and decorate numbers: {', '.join(items)}!\"",
        },
        {
            "code": "W292",
            "filename": "./source_code_2.py",
            "line_number": 18,
            "column_number": 100,
            "text": "no newline at end of file",
            "physical_line": '    return f"I like to filter, rounding, doubling, '
            "store and decorate numbers: {', '.join(items)}!\"",
        },
    ]
}

print(format_linter_error(error=errors_))
# print(list(errors["./source_code_2.py"][0].keys()))













a = {"a": [
        {
            "code": "E501",
            "filename": "./source_code_2.py",
            "line_number": 18,
            "column_number": 80,
            "text": "line too long (99 > 79 characters)",
            "physical_line": '    return f"I like to filter, rounding, doubling, '
            "store and decorate numbers: {', '.join(items)}!\"",
        },
    ]
}
print(len(a["a"]))