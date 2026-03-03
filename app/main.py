def format_linter_error(error: dict) -> dict:
    return \
        {
            "line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "flake8"
        }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return \
        {
            "errors":
                [
                    {
                        "line": key["line_number"],
                        "column": key["column_number"],
                        "message": key["text"],
                        "name": key["code"],
                        "source": "flake8"
                    }
                    for key in errors
                ],
            "path": file_path,
            "status": "failed" if errors != [] else "passed"

        }


def format_linter_report(linter_report: dict) -> list:
    return \
        [
            format_single_linter_file(
                "./test_source_code_2.py",
                linter_report["./test_source_code_2.py"]
            ),

            format_single_linter_file(
                "./source_code_2.py",
                linter_report["./source_code_2.py"]
            ),

            format_single_linter_file(
                "./source_code_1.py",
                linter_report["./source_code_1.py"]
            ),

            format_single_linter_file(
                "./test_source_code_1.py",
                linter_report["./test_source_code_1.py"]
            )
        ]
