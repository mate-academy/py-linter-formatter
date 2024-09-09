def format_linter_error(error: dict) -> dict:
    return {
        (
            "name" if key == "code" else "source" if key == "filename" else
            "message" if key == "text" else
            tuple(key.split("_"))[0]
        ):
        ("flake8" if key == "filename" else value)
        for key, value in error.items() if
        value is not None and key != "physical_line"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed" if errors else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(filepath, errors)
        for filepath, errors in linter_report.items()
    ]
