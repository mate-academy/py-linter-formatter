from typing import List, Dict, Any


def format_linter_error(error: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(
        file_path: str,
        errors: List[Dict[str, Any]]) -> Dict[str, Any]:
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed" if errors else "passed"
    }


def format_linter_report(
        linter_report: Dict[str, Any]) -> List[Dict[str, Any]]:
    return [format_single_linter_file(file_path, errors)
            for file_path, errors in linter_report.items()]
