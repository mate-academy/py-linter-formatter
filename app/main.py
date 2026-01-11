def format_linter_error(error: dict) -> dict:
    # write your code here
    # The slash \ is used after "else"s
    # #to avoid "\n" errors in the long ternary operators
    return {key : error[val] for key, val
            in
            {
                "line" : "line_number",
                "column" : "column_number",
                "message" : "text",
                "name" : "code"}.items()
            }\
        | {"source" : "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # write your code here
    return {"errors": {}, "path": file_path, "status": "passed"}\
        if not errors else\
        {"errors": [format_linter_error(error) for error in errors],
         "path": file_path, "status": "failed"}


def format_linter_report(linter_report: dict) -> list:
    # write your code here
    return [
        {
            key : {
                "errors": [],
                "path": key,
                "status": "passed"
            } if not val else {
                key: {
                    "errors": [
                        format_linter_error(error)
                        for error in linter_report[key]],
                    "path": key,
                    "status": "failed"
                }
            }
            for key, val in linter_report.items()
        }
    ]
