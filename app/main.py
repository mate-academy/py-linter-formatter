def format_linter_error(error: dict) -> dict:
    return {"line": error.get("line_number", 0), "column": error.get("column_number", 0), "message": error.get("text", ""), "name": error.get("code", ""), "source": "flake8"}




def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"path": file_path, "status": "failed" if errors else "passed", "errors": [format_linter_error(error) for error in errors]}



def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(path, linter_report[path]) for path in ["./test_source_code_2.py", "./source_code_2.py", "./source_code_1.py", "./test_source_code_1.py"] if path in linter_report]

