from typing import List, Dict, Any, Union


def format_linter_error(
    error: Dict[str, Union[int, str]]
) -> Dict[str, Union[int, str]]:
    return {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code"),
        "source": "flake8",
    }


def format_single_linter_file(
        file_path: str, errors: List[Dict[str, Any]]
) -> Dict[str, Any]:
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed" if errors else "passed",
    }


def format_linter_report(
        linter_report: Dict[str, List[Dict[str, Any]]]
) -> List[Dict[str, Any]]:
    return [
        format_single_linter_file(file_path, linter_report[file_path])
        for file_path in linter_report
    ]
