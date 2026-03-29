def format_linter_error(e: dict) -> dict:
    return {
        "line": e["line_number"],
        "column": e["column_number"],
        "message": e["text"],
        "name": e["code"],
        "source": "flake8",
    }

def format_single_linter_file(fp: str, es: list[dict]) -> dict:
    return {
        "errors": [format_linter_error(e) for e in es],
        "path": fp,
        "status": "failed" if es else "passed",
    }

def format_linter_report(r: dict[str, list[dict]]) -> list[dict]:
    return [format_single_linter_file(fp, es) for fp, es in r.items()]
