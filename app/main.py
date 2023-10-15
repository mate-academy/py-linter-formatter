def format_linter_error(error: dict) -> dict:
    return {"line" if key == "line_number" else
            "column" if key == "column_number" else
            "message" if key == "text" else
            "name" if key == "code" else
            "source": "flake8" if key == "physical_line" else
            val for key, val in (error.items())}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [format_linter_error(error) for error in errors],
            "path": file_path,
            "status": "passed" if len(errors) == 0 else "failed"}


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": linter_report[key],
            "path": key,
            "status": "passed" if (len(linter_report[key]) == 0) else "failed"
        } if item == [] else
        format_single_linter_file(key, linter_report[key])
        for (key, item) in linter_report.items()
    ]
