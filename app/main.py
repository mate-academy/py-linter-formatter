def format_linter_error(error: dict) -> dict:
    return(
        {
            "column": error["column_number"],
            "line": error["line_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "flake8",
        }
    )
    pass


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return(
        {
            "errors":
            [
                {
                    "column": errors[number]["column_number"],
                    "line": errors[number]["line_number"],
                    "message": errors[number]["text"],
                    "name": errors[number]["code"],
                    "source": "flake8",
                }
                for number in range(len(errors))
            ],
            "path": file_path,
            "status": ("failed" if errors else "passed"),
        }
    )
    pass


def format_linter_report(linter_report: dict) -> list:
    return(
        [
            {
                "errors":
                [
                    {
                        "column": name["column_number"],
                        "line": name["line_number"],
                        "message": name["text"],
                        "name": name["code"],
                        "source": "flake8",
                    }
                    for name in value
                ],
                "path": key,
                "status": ("failed" if value else "passed"),
            }
            for key, value in linter_report.items()
        ]
    )
    pass
