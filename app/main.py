def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    erro_formatado = [format_linter_error(e) for e in errors]
    status = "failed" if erro_formatado else "passed"
    return {
        "errors": erro_formatado,
        "path": file_path,
        "status": status
    }



def format_linter_report(linter_report: dict) -> list:
    pass