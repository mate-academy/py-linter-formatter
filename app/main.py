def format_linter_error(error: dict) -> dict:
    return
    {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return
    {
        file_path:
        [
            format_linter_error(errors[i])
            for i in range(len(errors))
        ]
    }


def format_linter_report(linter_report: dict) -> list:
    return
    [
        {
            "errors": format_single_linter_file(key, value)[key],
            "path": key,
            "status": "passed" if len(value) == 0 else "failed"
        }
        for i in range(len(linter_report))
        for key, value in linter_report.items()
    ]
