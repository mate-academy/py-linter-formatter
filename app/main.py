# def format_linter_error(error: dict) -> dict:
#     return {
#     "line": error.get("line_number"),
#     "column": error.get("column_number"),
#     "message": error.get("text"),
#     "name": error.get("code"),
#     "source": "flake8"
#     }


# def format_single_linter_file(file_path: str, errors: list) -> dict:
#     print(len(errors))
#     return {"errors":
#         [
#             {"line": error_dict["line_number"],
#              "column": error_dict["column_number"],
#              "message": error_dict["text"],
#              "name": error_dict["code"],
#              "source": "flake8"
#              }
#             for error_dict in errors
#
#         ],
#         "path": file_path,
#         "status": "failed" if len(errors) > 0 else "passed"
#     }


def format_linter_report(linter_report: dict) -> list:
    return [
    {
        "errors": linter_report.get("./test_source_code_2.py"),
        "path": key for k,v?
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

# error = {
#     "code": "E501",
#     "filename": "./source_code_2.py",
#     "line_number": 18,
#     "column_number": 80,
#     "text": "line too long (99 > 79 characters)",
#     "physical_line": '    return f"I like to filter, rounding, doubling, '
#     "store and decorate numbers: {', '.join(items)}!\"",
# }
# print(format_linter_error(error=error))

# errors = [
#     {
#         "code": "E501",
#         "filename": "./source_code_2.py",
#         "line_number": 18,
#         "column_number": 80,
#         "text": "line too long (99 > 79 characters)",
#         "physical_line": '    return f"I like to filter, rounding, doubling, '
#                          "store and decorate numbers: {', '.join(items)}!\"",
#     },
#     {
#         "code": "W292",
#         "filename": "./source_code_2.py",
#         "line_number": 18,
#         "column_number": 100,
#         "text": "no newline at end of file",
#         "physical_line": '    return f"I like to filter, rounding, doubling, '
#                          "store and decorate numbers: {', '.join(items)}!\"",
#     },
# ]
# print(format_single_linter_file(file_path="./source_code_2.py", errors=errors))

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