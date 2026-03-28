from typing import List, Dict, Any


def format_linter_error(error: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "name": error.get("code"),
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "source": "flake8",
    }


def format_single_linter_file(
    file_path: str,
    errors: List[Dict[str, Any]]
) -> Dict[str, Any]:
    return {
        "path": file_path,
        "errors": [
            format_linter_error(error)
            for error in errors
        ],
        "status": "passed" if not errors else "failed",
    }


def format_linter_report(
    linter_report: Dict[str, List[Dict[str, Any]]]
) -> List[Dict[str, Any]]:
    return [
        format_single_linter_file(file_path, errors)
        for file_path, errors in linter_report.items()
    ]
