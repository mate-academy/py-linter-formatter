def format_linter_error(error: dict) -> dict:
    return {"line" if key == "line_number" else
            "column" if key == "column_number" else
            "message" if key == "text" else
            "name" if key == "code" else
            "source": error[key] if key != "filename" else "flake8"
            for key in error
            if key == "code" or key == "column_number"
            or key == "line_number" or key == "text" or key == "filename"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [format_linter_error(error) for error in errors],
            "path": file_path,
            "status": "passed" if errors == [] else "failed"}


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(file_path=key, errors=linter_report[key])
            for key in linter_report]
