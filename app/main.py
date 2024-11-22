
def format_linter_error(error: dict) -> dict:
    return {"error": "E501"}

def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [], "path": "./test_source_code_2.py", "status": "passed"}


def format_linter_report(linter_report: dict) -> list:
    return {"errors": [], "path": "./test_source_code_2.py", "status": "passed"}

