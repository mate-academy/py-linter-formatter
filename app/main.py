def format_linter_error(error: dict) -> dict:
    # write your code here
    return {
        "line" : error["line_number"],
        "column" : error["column_number"],
        "message" : error["message"],
        "name" : error["code"],
        "source" : "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors" :
            [
                {
                    format_linter_error(error) for error in errors
                }
            ],
        "path" : file_path,
        "status" : "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors" : linter_report["/test_source_code_2"],
            "path" : linter_report["path"],
        }
    ]
