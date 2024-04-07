from typing import Dict, List


def format_linter_error(error: Dict) -> Dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: List[Dict]) -> Dict:
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed" if errors else "passed"
    }


def format_linter_report(linter_report: Dict[str, List[Dict]]) -> List[Dict]:
    return [format_single_linter_file(file_path, errors)
            for file_path, errors in linter_report.items()]
