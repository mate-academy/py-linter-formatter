def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors":
            [
                {
                    "line": errors[0]["line_number"],
                    "column": errors[0]["column_number"],
                    "message": errors[0]["text"],
                    "name": errors[0]["code"],
                    "source": "flake8"
                },
                {
                    "line": errors[1]["line_number"],
                    "column": errors[1]["column_number"],
                    "message": errors[1]["text"],
                    "name": errors[1]["code"],
                    "source": "flake8"
                }
            ],
        "path": file_path,
        "status": "failed" if len(errors) > 0 else "passed"
    }


def format_linter_report(errors_linter: dict) -> list:
    return [
        {
            errors_linter[0]["errors"]: [],
            errors_linter[0][
                "path"]: "./test_source_code_2.py",
            errors_linter[0]["status"]: "passed"
        },
        {
            errors_linter[1]["errors"]:
                [
                    {
                        "line": errors_linter[1][0][
                            "line_number"],
                        "column": errors_linter[1][0][
                            "column_number"],
                        "message": errors_linter[1][0][
                            "text"],
                        "name": errors_linter[1][0][
                            "code"],
                        "source": "flake8"
                    },
                    {
                        "line": errors_linter[1][1][
                            "line_number"],
                        "column": errors_linter[1][1][
                            "column_number"],
                        "message": errors_linter[1][1][
                            "text"],
                        "name": errors_linter[1][1][
                            "code"],
                        "source": "flake8"
                    }
                ],
            "path": "./source_code_2.py",
            "status": "failed"
        }
    ]
