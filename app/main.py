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




def format_linter_report(linter_report: dict) -> list:
    # write your code here
    return [
        {
            "errors": list(),
            "path": list(linter_report.keys())[0],
            "status": "passed"

        },
        # linter_report.get("./source_code_2.py")
        # format_single_linter_file(list(linter_report.keys())[0], data)
        # никак не могу понять как сделать правильно !!!!!
        [format_single_linter_file(list(linter_report.keys())[i], data) for i, data in enumerate(list(linter_report.values())) if i>0]
        # format_single_linter_file(list(linter_report.keys())[0], list(linter_report.values())[2])
        # for i, data in enumerate(list(linter_report.values())):
        #     if i > 0:
        #         format_single_linter_file(list(linter_report.keys())[i], data)




    ]