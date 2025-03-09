update_error_local = {
    "line_number": "line",
    "column_number": "column",
    "text": "message",
    "code": "name",
    "flake8": "source"
}


def format_linter_error(error: dict) -> dict:
    return {
        value: (error[key] if key in error else key)
        for key, value in update_error_local.items()
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [{value: (i[key] if key in i else key)
                   for key, value in update_error_local.items()}
                   for i in errors],
        "path": file_path,
        "status": "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {"errors": linter_report[i]
        if linter_report[i] == []
        else [{value: (error[key] if key in error else key)
               for key, value in update_error_local.items()}
              for error in linter_report[i]]
            , "path": i, "status": "passed"
        if linter_report[i] == []
        else "failed"
         }
        for i in linter_report]


error = {
    "code": "E501",
    "filename": "./source_code_2.py",
    "line_number": 18,
    "column_number": 80,
    "text": "line too long (99 > 79 characters)",
    "physical_line": "    return f\"I like to filter, rounding, doubling, "
                     "store and decorate numbers: {\", \".join(items)}!\"",
}

errors = [
    {
        "code": "E501",
        "filename": "./source_code_2.py",
        "line_number": 18,
        "column_number": 80,
        "text": "line too long (99 > 79 characters)",
        "physical_line": "    return f\"I like to filter, rounding, doubling, "
                         "store and decorate numbers: {\", \".join(items)}!\"",
    },
    {
        "code": "W292",
        "filename": "./source_code_2.py",
        "line_number": 18,
        "column_number": 100,
        "text": "no newline at end of file",
        "physical_line": "    return f\"I like to filter, rounding, doubling, "
                         "store and decorate numbers: {\", \".join(items)}!\"",
    },
]

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
                "physical_line":
                        "    return f\"I like to filter, rounding, doubling, "
                        "store and decorate numbers: {\", \".join(items)}!\"",
            },
            {
                "code": "W292",
                "filename": "./source_code_2.py",
                "line_number": 18,
                "column_number": 100,
                "text": "no newline at end of file",
                "physical_line":
                        "    return f\"I like to filter, rounding, doubling, "
                        "store and decorate numbers: {\", \".join(items)}!\"",
            },
    ]
}


print(format_linter_error(error=error))
print(format_single_linter_file(file_path="./source_code_2.py", errors=errors))
print(format_linter_report(linter_report=report_file))
