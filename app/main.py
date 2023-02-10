def format_linter_error(error: dict) -> dict:
    error = {
        "code": "E501",
        "filename": "./source_code_2.py",
        "line_number": 18,
        "column_number": 80,
        "text": "line too long (99 > 79 characters)",
        "physical_line": '    return f"I like to filter, rounding, doubling, '
                         "store and decorate numbers: {', '.join(items)}!\"",
    }

    print(format_linter_error(error=error))
    # The output will be:
    {
        "line": 18,
        "column": 80,
        "message": "line too long (99 > 79 characters)",
        "name": "E501",
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    errors = [
        {
            "code": "E501",
            "filename": "./source_code_2.py",
            "line_number": 18,
            "column_number": 80,
            "text": "line too long (99 > 79 characters)",
            "physical_line": '    return f"I like to filter, rounding, doubling, '
                             "store and decorate numbers: {', '.join(items)}!\"",
        },
        {
            "code": "W292",
            "filename": "./source_code_2.py",
            "line_number": 18,
            "column_number": 100,
            "text": "no newline at end of file",
            "physical_line": '    return f"I like to filter, rounding, doubling, '
                             "store and decorate numbers: {', '.join(items)}!\"",
        },
    ]

    print(format_single_linter_file(file_path="./source_code_2.py", errors=errors))
    # The output will be:
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

def format_linter_report(linter_report: dict) -> list:
    report_file = {
        "./test_source_code_2.py": [],
        "./source_code_2.py":
            [
                {
                    "code": "E501",
                    "filename": "./source_code_2.py",
                    "line_number": 18,
                    "column_number": 80,
                    "text": "line too long (99 > 79 characters)",
                    "physical_line": '    return f"I like to filter, rounding, doubling, '
                                     "store and decorate numbers: {', '.join(items)}!\"",
                },
                {
                    "code": "W292",
                    "filename": "./source_code_2.py",
                    "line_number": 18,
                    "column_number": 100,
                    "text": "no newline at end of file",
                    "physical_line": '    return f"I like to filter, rounding, doubling, '
                                     "store and decorate numbers: {', '.join(items)}!\"",
                },
            ]
    }

    print(format_linter_report(linter_report=report_file))
    # The output will be:
    [
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

    errors = [
        {"errors": [], "path": "./test_source_code_2.py", "status": "passed"},
        {
            "errors": [
                {
                    "line": 18,
                    "column": 80,
                    "message": "line too long (99 > 79 characters)",
                    "name": "E501",
                    "source": "flake8",
                },
                {
                    "line": 18,
                    "column": 100,
                    "message": "no newline at end of file",
                    "name": "W292",
                    "source": "flake8",
                },
            ],
            "path": "./source_code_2.py",
            "status": "failed",
        },
        {
            "errors": [
                {
                    "line": 3,
                    "column": 74,
                    "message": "multiple statements on one line (semicolon)",
                    "name": "E702",
                    "source": "flake8",
                },
                {
                    "line": 3,
                    "column": 80,
                    "message": "line too long (97 > 79 characters)",
                    "name": "E501",
                    "source": "flake8",
                },
                {
                    "line": 15,
                    "column": 1,
                    "message": "expected 2 blank lines, found 1",
                    "name": "E302",
                    "source": "flake8",
                },
                {
                    "line": 27,
                    "column": 1,
                    "message": "too many blank lines (6)",
                    "name": "E303",
                    "source": "flake8",
                },
                {
                    "line": 31,
                    "column": 80,
                    "message": "line too long (99 > 79 characters)",
                    "name": "E501",
                    "source": "flake8",
                },
            ],
            "path": "./source_code_1.py",
            "status": "failed",
        },
        {
            "errors": [
                {
                    "line": 4,
                    "column": 1,
                    "message": "expected 2 blank lines, found 1",
                    "name": "E302",
                    "source": "flake8",
                },
                {
                    "line": 32,
                    "column": 80,
                    "message": "line too long (84 > 79 characters)",
                    "name": "E501",
                    "source": "flake8",
                },
                {
                    "line": 112,
                    "column": 6,
                    "message": "no newline at end of file",
                    "name": "W292",
                    "source": "flake8",
                },
            ],
            "path": "./test_source_code_1.py",
            "status": "failed",
        },
    ]
