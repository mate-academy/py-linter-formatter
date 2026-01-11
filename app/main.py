def format_linter_error(error: dict) -> dict:
    # write your code here
    return {error_param: data for error_param, data in
            {"line": error["line_number"], "column": error["column_number"],
             "message": error["text"], "name": error["code"], "source": "flake8"}.items()}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # write your code here
    return {"errors": [format_linter_error(error) for error in errors],
            "path": file_path, "status": "passed" if not errors else "failed"}


def format_linter_report(linter_report: dict) -> list:
    # write your code here
    return [format_single_linter_file(error_data[0], error_data[1])
            for error_data in linter_report.items()]
