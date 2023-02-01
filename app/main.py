def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["physical_line"],
            "source": error["store and decorate numbers"]}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    result = {"errors": [format_linter_error(errors[index])]
              for index in enumerate(errors)}
    result["path"] = file_path
    result["status"] = "failed" if errors != [] else "passed"
    return result


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(element) for element in linter_report]
