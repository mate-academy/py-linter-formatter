error_key_map = {
    "line_number": "line",
    "column_number": "column",
    "text": "message",
    "code": "name"
}


def format_linter_error(error: dict) -> dict:
    return {error_key_map.get(key): value for key, value in error.items()
            if key in error_key_map} | {"source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [format_linter_error(error) for error in errors]}\
        | {"path": file_path, "status": ("passed" if errors == []
                                         else "failed")}


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(key, value)
            for key, value in linter_report.items()]
