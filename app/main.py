def format_linter_error(error: dict) -> dict:
    return {("line" if ky == "line_number" else "column"
            if ky == "column_number" else "message"
            if ky == "text" else "name"
            if ky == "code" else "source"):
                (vl if ky in ["line_number", "column_number",
                              "text", "code"] else "flake8")
            for ky, vl in error.items()}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors" : [format_linter_error(error) for error in errors],
            "path": file_path, "status": ("failed" if errors else "passed")}


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(file, errors) for file,
            errors in linter_report.items()]
