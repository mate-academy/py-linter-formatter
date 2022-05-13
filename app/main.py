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
        "errors": [
            {
                "line": error["line_number"],
                "column": error["column_number"],
                "message": error["text"],
                "name": error["code"],
                "source": "flake8",
            }
            for error in errors
        ],
        "path": file_path,
        "status": "passed" if len(errors) == 0 else "failed",
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [
                {
                    "line": report[i]["line_number"],
                    "column": report[i]["column_number"],
                    "message": report[i]["text"],
                    "name": report[i]["code"],
                    "source": "flake8",
                }
                for i in range(len(report))
            ],
            "path": key,
            "status": "passed" if len(report) == 0 else "failed",
        }
        for key, report in linter_report.items()
    ]

