def format_linter_error(error: dict) -> dict:
    return dict(line=error["line_number"],
                column=error["column_number"],
                message=error["text"],
                name=error["code"],
                source="flake8")


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [
        dict(line=error["line_number"],
             column=error["column_number"],
             message=error["text"],
             name=error["code"],
             source="flake8")
        for error in errors],
        "path": file_path,
        "status": "passed" if not errors else "failed", }


def format_linter_report(linter_report: dict) -> list[dict]:
    return [{"errors": [
        dict(line=error["line_number"],
             column=error["column_number"],
             message=error["text"],
             name=error["code"],
             source="flake8")
        for error in path],
        "path":path_name,
        "status": "passed" if not path else "failed", }
        for path_name, path in linter_report.items()]
