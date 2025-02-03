<<<<<<< HEAD
def format_linter_error(error):
=======
<<<<<<< HEAD
def format_linter_error(error: dict) -> dict:
=======
def format_linter_error(error):
>>>>>>> bbb2505 (Solution)
>>>>>>> 98b789f (Solution)
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8",
    }


<<<<<<< HEAD
def format_single_linter_file(file_path, errors):
=======
<<<<<<< HEAD
def format_single_linter_file(file_path: str, errors: list) -> dict:
=======
def format_single_linter_file(file_path, errors):
>>>>>>> bbb2505 (Solution)
>>>>>>> 98b789f (Solution)
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed" if errors else "passed",
    }


<<<<<<< HEAD
def format_linter_report(linter_report):
=======
<<<<<<< HEAD
def format_linter_report(linter_report: dict) -> list:
=======
def format_linter_report(linter_report):
>>>>>>> bbb2505 (Solution)
>>>>>>> 98b789f (Solution)
    return [
        format_single_linter_file(file_path, errors)
        for file_path, errors in linter_report.items()
    ]
