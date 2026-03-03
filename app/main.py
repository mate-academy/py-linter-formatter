# Импорты должны находиться на самом верху файла
from typing import List, Dict


def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8",
    }


def format_single_linter_file(file_path: str, errors: List[dict]) -> dict:
    return {
        "errors": [
            {
                "line": error["line_number"],
                "column": error["column_number"],
                "message": error["text"],
                "name": error["code"],
                "source": "flake8",
            }
            for error in errors
        ],
        "path": file_path,
        "status": "failed" if errors else "passed",
    }


def format_linter_report(linter_report: Dict[str, List[dict]]) -> List[dict]:
    return [
        format_single_linter_file(file_path, errors)
        for file_path, errors in linter_report.items()
    ]
