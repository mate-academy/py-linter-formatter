def format_linter_error(error: dict) -> dict:
    return {
        new_key: error[old_key] if new_key != "source" else "flake8"
        for old_key, new_key in
        zip(("line_number", "column_number", "text", "code", None),
            ("line", "column", "message", "name", "source"))
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        key: "failed" if (key == "status" and errors) else value
        for key, value in [
            ("errors", [format_linter_error(error) for error in errors]),
            ("path", file_path),
            ("status", "passed")
        ]
    }


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(path, errors)
            for path, errors in linter_report.items()]
