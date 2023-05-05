def format_linter_error(error: dict) -> dict:
    return {
        n_key: error[old] if old in error else old for n_key, old in zip(
            ["line", "column", "message", "name", "source"],
            ["line_number", "column_number", "text", "code", "flake8"]
        )
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        n_key: n_value for n_key, n_value in zip(
            ["errors", "path", "status"],
            [
                [format_linter_error(err) for err in errors],
                file_path,
                "failed" if errors != [] else "passed"
            ]
        )
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(key, value)
        for key, value in linter_report.items()
    ]
