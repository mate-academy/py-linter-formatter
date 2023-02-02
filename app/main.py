def format_linter_error(error: dict) -> dict:
    return {
        "line": 18,
        "column": 80,
        "message": "line too long (99 > 79 characters)",
        "name": "E501",
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
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
        "status": "failed"
    }
    ]
