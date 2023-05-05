def format_linter_error(error: dict) -> dict:
    return {
        new_key: error[old_key] if old_key in error else old_key
        for new_key, old_key in zip(
            ["line", "column", "message", "name", "source"],
            ["line_number", "column_number", "text", "code", "flake8"]
        )
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        new_key: new_value for new_key, new_value in zip(
            ["errors", "path", "status"],
            [
                [format_linter_error(error) for error in errors],
                file_path,
                "failed" if errors != [] else "passed"
            ]
        )
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file_path_as_key, errors_as_value)
        for file_path_as_key, errors_as_value in linter_report.items()
    ]
