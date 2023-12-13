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
        "errors": [format_linter_error(error_dict) for error_dict in errors],
        "path": file_path,
        "status": "failed" if len(errors) else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": linter_report[[key for key in linter_report][0]],
            "path": [key for key in linter_report][0],
            "status": "failed" if linter_report[[key for key in linter_report][0]] else "passed"
        },
        format_single_linter_file([key for key in linter_report][1], linter_report[[key for key in linter_report][1]])
    ]

error = {
    "code": "E501",
    "filename": "./source_code_2.py",
    "line_number": 18,
    "column_number": 80,
    "text": "line too long (99 > 79 characters)",
    "physical_line": '    return f"I like to filter, rounding, doubling, '
                     "store and decorate numbers: {', '.join(items)}!\"",
}

print(1, format_linter_error(error))

errors2 = [
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

print(2, format_single_linter_file("./source_code_2.py", errors2))

# comment
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

print(3, format_linter_report(report_file))
# The output will be:
"""
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
"""
