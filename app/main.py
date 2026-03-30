def format_linter_error(error: dict) -> dict:
    return dict(zip(("line", "column", "message", "name", "source"),
                    (error["line_number"],
                     error["column_number"],
                     error["text"],
                     error["code"],
                     "flake8"
                     )))


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return dict(
        zip(
            ("errors", "path", "status"),
            (
                [format_linter_error(error) for error in errors],
                file_path, "failed"
                if errors
                else "passed"
            )
        )
    )


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(key, report)
        for key, report in linter_report.items()
    ]
