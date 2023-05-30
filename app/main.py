
def format_linter_error(error: dict) -> dict:

    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


print(format_linter_error(
    {
        "code": "E501",
        "filename": "./source_code_2.py",
        "line_number": 18,
        "column_number": 80,
        "text": "line too long (99 > 79 characters)",
        "physical_line": "return f'I like to filter, rounding, doubling, "
        "store and decorate numbers: {', '.join(items)}!\""
    }
)
)


def format_single_linter_file(file_path: str, errors: list) -> dict:

    return {"errors":
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


print(format_single_linter_file(file_path="./source_code_2.py", errors=[
    {
        "code": "E501",
        "filename": "./source_code_2.py",
        "line_number": 18,
        "column_number": 80,
        "text": "line too long (99 > 79 characters)",
        "physical_line": "return f'I like to filter, rounding, doubling,"
        "store and decorate numbers: {', '.join(items)}!\""
    },
    {
        "code": "W292",
        "filename": "./source_code_2.py",
        "line_number": 18,
        "column_number": 100,
        "text": "no newline at end of file",
        "physical_line": "return f'I like to filter, rounding, doubling,"
        "store and decorate numbers: {', '.join(items)}!\""
    },
]))


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": linter_report["./test_source_code_2.py"],
            "path": "./test_source_code_2.py",
            "status": "passed"
        },
        {
            "errors":
            [
                {
                    "line":
                    linter_report["./source_code_2.py"][0]["line_number"],
                    "column":
                    linter_report["./source_code_2.py"][0]["column_number"],
                    "message":
                    linter_report["./source_code_2.py"][0]["text"],
                    "name":
                    linter_report["./source_code_2.py"][0]["code"],
                    "source":
                    "flake8"
                },
                {
                    "line":
                    linter_report["./source_code_2.py"][1]["line_number"],
                    "column":
                    linter_report["./source_code_2.py"][1]["column_number"],
                    "message":
                    linter_report["./source_code_2.py"][1]["text"],
                    "name":
                    linter_report["./source_code_2.py"][1]["code"],
                    "source":
                    "flake8"
                }
            ],
            "path": "./source_code_2.py",
            "status": "failed"
        }
    ]


print(format_linter_report(linter_report={
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
                    "return f'I like to filter, rounding, doubling,"
                "store and decorate numbers: {', '.join(items)}!\""
            },
            {
                "code": "W292",
                "filename": "./source_code_2.py",
                "line_number": 18,
                "column_number": 100,
                "text": "no newline at end of file",
                "physical_line":
                    "return f'I like to filter, rounding, doubling,"
                "store and decorate numbers: {', '.join(items)}!\""
            },
    ]
}))
