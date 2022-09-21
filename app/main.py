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
        "status": "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [{
        "errors": [],
        "path": "./test_source_code_2.py",
        "status": "passed"
    },
        {
        "errors":
            [
                {
                    "line": 18,
                    "column": 80,
                    "message": "line too long (99 > 79 characters)",
                    "name": "E501",
                    "source": "flake8"
                },
                {
                    "line": 18,
                    "column": 100,
                    "message": "no newline at end of file",
                    "name": "W292",
                    "source": "flake8"
                }
            ],
        "path": "./source_code_2.py",
        "status": "failed"},
        {"errors": [{"column": 74,
                     "line": 3,
                     "message": "multiple statements on one line (semicolon)",
                     "name": "E702",
                     "source": "flake8"},
                    {"column": 80,
                     "line": 3,
                     "message": "line too long (97 > 79 characters)",
                     "name": "E501",
                     "source": "flake8"},
                    {"column": 1,
                     "line": 15,
                     "message": "expected 2 blank lines, found 1",
                     "name": "E302",
                     "source": "flake8"},
                    {"column": 1,
                     "line": 27,
                     "message": "too many blank lines (6)",
                     "name": "E303",
                     "source": "flake8"},
                    {"column": 80,
                     "line": 31,
                     "message": "line too long (99 > 79 characters)",
                     "name": "E501",
                     "source": "flake8"}],
         "path": "./source_code_1.py",
         "status": "failed"},
        {"errors": [{"column": 1,
                     "line": 4,
                     "message": "expected 2 blank lines, found 1",
                     "name": "E302",
                     "source": "flake8"},
                    {"column": 80,
                     "line": 32,
                     "message": "line too long (84 > 79 characters)",
                     "name": "E501",
                     "source": "flake8"},
                    {"column": 6,
                     "line": 112,
                     "message": "no newline at end of file",
                     "name": "W292",
                     "source": "flake8"}],
         "path": "./test_source_code_1.py",
         "status": "failed"}]
