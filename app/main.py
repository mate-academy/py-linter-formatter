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
                "line": errors[a]["line_number"],
                "column": errors[a]["column_number"],
                "message": errors[a]["text"],
                "name": errors[a]["code"],
                "source": "flake8",
            }
            for a in range(len(errors))
        ],
        "path": file_path,
        "status": "passed" if errors == [] else "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [
                {
                    "line": list(linter_report.values())[i][a]["line_number"],
                    "column":
                        list(linter_report.values())[i][a]["column_number"],
                    "message": list(linter_report.values())[i][a]["text"],
                    "name": list(linter_report.values())[i][a]["code"],
                    "source": "flake8",
                }
                for a in range(len(list(linter_report.values())[i]))
            ],
            "path": list(linter_report.keys())[i],
            "status": "passed" if list(linter_report.values())[i] == []
            else "failed"
        }
        for i in range(len(linter_report))
    ]
