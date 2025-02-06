from typing import Any


def format_linter_error(error: dict) -> dict[str, str | Any]:
    return dict(line=error["line_number"],
                column=error["column_number"],
                message=error["text"],
                name=error["code"],
                source="flake8")


def format_single_linter_file(file_path: str, errors: list) \
        -> dict[str, list[dict[str, str | Any]] | str]:
    return dict(errors=[format_linter_error(error) for error in errors],
                path=file_path,
                status="failed" if errors
                else "passed")


def format_linter_report(linter_report: dict) -> list:
    return [
        dict(
            errors=linter_report["./test_source_code_2.py"],
            path="./test_source_code_2.py",
            status="failed" if errors_list
            else "passed"
        ) | (format_single_linter_file(file_path, errors_list))
        for file_path, errors_list in linter_report.items()
    ]
