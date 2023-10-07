def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8",
    }



def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors":
            [
                {
                    "line": error["line_number"],
                    "column": error["column_number"],
                    "message": error["text"],
                    "name": error["code"],
                    "source": "flake8",
                }
                for error in errors
            ],
        "path": errors[0]["filename"],
        "status": "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        [
            {
                "errors":
                    [
                        {
                            "line": error["line_number"],
                            "column": error["column_number"],
                            "message": error["text"],
                            "name": error["code"],
                            "source": "flake8",
                        }
                    ],
                "path": file_name,
                "status": "passed" if not result else "failed"
            }
            for error in result
        ]
        for file_name, result in linter_report.items()
    ]
