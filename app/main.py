def format_linter_error(error: dict) -> dict:

    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8",
    }


error = {
    "code": "E501",
    "filename": "./source_code_2.py",
    "line_number": 18,
    "column_number": 80,
    "text": "line too long (99 > 79 characters)",
    "physical_line": """    return f"I like to filter,
    rounding, doubling,
    store and decorate numbers: {", ".join(items)}!\"""",
}

print(format_linter_error(error=error))


def format_single_linter_file(file_path: str, errors: list) -> dict:

    return {
        "errors": [format_linter_error(er) for er in errors],
        "path": file_path,
        "status": "failed" if errors else "passed",
    }


errors = [
    {
        "code": "E501",
        "filename": "./source_code_2.py",
        "line_number": 18,
        "column_number": 80,
        "text": "line too long (99 > 79 characters)",
        "physical_line": """    return f"I like to filter,
        rounding, doubling,
        store and decorate numbers: {", ".join(items)}!\"""",
    },
    {
        "code": "W292",
        "filename": "./source_code_2.py",
        "line_number": 18,
        "column_number": 100,
        "text": "no newline at end of file",
        "physical_line": """    return f"I like to filter,
        rounding, doubling,
        store and decorate numbers: {", ".join(items)}!\"""",
    },
]

print(format_single_linter_file(file_path="./source_code_2.py", errors=errors))


def format_linter_report(linter_report: dict) -> list:

    return [
        format_single_linter_file(file_path=path, errors=errors)
        for path, errors in linter_report.items()
    ]


report_file = {
    "./test_source_code_2.py": [],
    "./source_code_2.py": [
        {
            "code": "E501",
            "filename": "./source_code_2.py",
            "line_number": 18,
            "column_number": 80,
            "text": "line too long (99 > 79 characters)",
            "physical_line": """    return f"I like to filter,
            rounding, doubling,
            store and decorate numbers: {", ".join(items)}!\"""",
        },
        {
            "code": "W292",
            "filename": "./source_code_2.py",
            "line_number": 18,
            "column_number": 100,
            "text": "no newline at end of file",
            "physical_line": """    return f"I like to filter,
            rounding, doubling,
            store and decorate numbers: {", ".join(items)}!\"""",
        },
    ],
}


print(format_linter_report(linter_report=report_file))
