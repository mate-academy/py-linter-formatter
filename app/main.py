def format_linter_error(error: dict) -> dict:
    return {("name" if key == "code"
             else "line" if key == "line_number"
             else "column" if key == "column_number"
             else "message" if key == "text"
             else "source"): ("flake8" if str(value).startswith("./s") else value)
            for key, value in (dict(list(error.items())[2:5] + list(error.items())[:2])).items()
            }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # write your code here
    pass


def format_linter_report(linter_report: dict) -> list:
    # write your code here
    pass
