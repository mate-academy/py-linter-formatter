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
        "errors": [
            {
                "line": error["line_number"],
                "column": error["column_number"],
                "message": error["text"],
                "name": error["code"],
                "source": "flake8"
            } for error in errors
        ],
        "path": file_path,
        "status": "passed" if not errors else "failed"}


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": linter_report["./test_source_code_2.py"],
            "path": "./test_source_code_2.py",
            "status": "passed" if not linter_report["./source_code_2.py"]
            else "failed"
        },
        [{
            "errors":
            [
                {
                    "line": int(error["line_number"]),
                    "column": error["column_number"],
                    "message": error["text"],
                    "name": error["code"],
                    "source": "flake8"
                } for error in errors],
            "path": "./source_code_2.py",
            "status": "passed" if not linter_report["./source_code_2.py"]
            else "failed"

        } for errors in linter_report["./source_code_2.py"]]
    ]
