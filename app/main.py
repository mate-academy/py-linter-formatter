def format_linter_error(error: dict) -> dict:
    return { # беру з error ті дані які потрібні для прінта і повертаю
        "line": error["line-number"],
        "column": error["column"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }

def format_single_linter_file(file_path: str, errors: list) -> dict:
    return  {
        "errors:" [
            [format_linter_error(error) for error in errors ]
        ],
        ["path": file_path,
        "status": "failed" if len(error) != 0 else "passed"]
    }
# Розумію що ця конструкція має получитись але не розумію як її зробити, 100% має бути if len(errors) == 0 "passed" else "failed"
# ше зрозумів що треба використовувати попередню конструкцію як вкладену
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

def format_linter_report(linter_report: dict) -> list:
    pass