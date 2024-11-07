def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"], "source": "flake8",
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [{
            "line": key["line_number"],
            "column": key["column_number"],
            "message": key["text"],
            "name": key["code"],
            "source": "flake8"
        } for key in errors],
        "path": file_path,
        "status": "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {"errors":
            [
                {
                    "line": key["line_number"],
                    "column": key["column_number"],
                    "message": key["text"],
                    "name": key["code"],
                    "source": "flake8"
                } for key in linter_report[file]],
            "path": file,
            "status": "passed" if not linter_report[file] else "failed"}
        for file in ["./test_source_code_2.py",
                     "./source_code_2.py",
                     "./source_code_1.py",
                     "./test_source_code_1.py"]]
