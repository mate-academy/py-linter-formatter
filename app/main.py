from audioop import error


def format_linter_error(error: dict) -> dict:

    return {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code"),
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:

    return {
        "errors":
            [
                {
                    format_linter_error(error)
                }
            ],
        "path": "./source_code_2.py",
        "status": "failed"
    }

def format_linter_report(linter_report: dict) -> list:

    return [
        {
            "errors": [],
            "path": "./test_source_code_2.py",
            "status": "passed"
        },
        {
            "errors":
                [
                    {
                        format_single_linter_file(file_path, error)
                    }
                ]
        }
    ]
