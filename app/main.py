def format_linter_error(error: dict) -> dict:
    # error = {
    #     "code": "E501",
    #     "filename": "./source_code_2.py",
    #     "line_number": 18,
    #     "column_number": 80,
    #     "text": "line too long (99 > 79 characters)",
    #     "physical_line": '    return f"I like to filter, rounding, doubling, '
    #                      "store and decorate numbers: {', '.join(items)}!\"",
    # }
    #
    # print(format_linter_error(error=error))

    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["name"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
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
    #
    # print(format_single_linter_file(file_path="./source_code_2.py", errors=errors))
# The output will be:
    # {
    #     "errors":
    #         [
    #             {
    #                 "line": 18,
    #                 "column": 80,
    #                 "message": "line too long (99 > 79 characters)",
    #                 "name": "E501",
    #                 "source": "flake8"
    #             },
    #             {
    #                 "line": 18,
    #                 "column": 100,
    #                 "message": "no newline at end of file",
    #                 "name": "W292",
    #                 "source": "flake8"
    #             }
    #         ],
    #     "path": "./source_code_2.py",
    #     "status": "failed"
    # }
    return {
        "errors": [
            format_linter_error(error) for error in errors
       ],
        "path": file_path,
        "status": "passed" if len(errors) == 0 else "failed"
    }

def format_linter_report(linter_report: dict) -> list:

#     return [

    [

    ]

     for path, errors in linter_report.items():
         for error in errors:


    "path": path,
    "status": >>>>>>>>>>>>>
         {"errors": [], "path": next(iter(linter_report)), "status": "passed"},
         {
             format_single_linter_file(path, value)
             for path, value in list(linter_report.items())[1]
         }
#     ]
"""
{
    "main.py": [
        {"line_number": 10, "column_number": 5, "text": "Missing whitespace", "code": "E201"}
    ],
    "utils.py": []
}

[
    {
        "errors": [
            {
                "line": 10,
                "column": 5,
                "message": "Missing whitespace",
                "name": "E201",
                "source": "flake8"
            }
        ],
        "path": "main.py",
        "status": "failed"
    },
    {
        "errors": [],
        "path": "utils.py",
        "status": "passed"
    }
]
"""