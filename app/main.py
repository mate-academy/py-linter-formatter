import importlib

print(importlib.import_module("pytest"))  # Альтернативний варіант

def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line"],
        "column": error["column"],
        "message": error["message"],
    }
print(format_linter_error({"line": 42, "column": 3, "message": "Syntax Error"}))


long_string = (
    "Цей рядок надто довгий і потрібно його розбити "
    "на два коротші, щоб відповідати стандарту PEP 8." )


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "path": file_path,
        "errors": [
            {
                "line": err["line_number"],
                "column": err["column_number"],
                "message": err["text"],
                "name": err["code"],
                "source": "flake8",
            }
            for err in errors
        ],
        "status": "failed" if errors else "passed",
    }

