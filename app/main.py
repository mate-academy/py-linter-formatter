def format_linter_error(error: dict) -> dict:
    return [{"errors": [{
        "line": error[key][i]["line_number"],
        "column": error[key][i]["column_number"],
        "message":error[key][i]["text"],
        "name": error[key][i]["code"],
        "source": "flake8"}if len(error[key]) else []
        for i in range(len(error[key]))],
        "path": key,
        "status": "failed"if len(error[key]) else"passed"}for key in error][0]


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return [{"errors": [{
        "line": errors[key][i]["line_number"],
        "column": errors[key][i]["column_number"],
        "message": errors[key][i]["text"],
        "name": errors[key][i]["code"],
        "source": "flake8"}
        if len(errors[key]) else []
        for i in range(len(errors[key]))],
        "path": key,
        "status": "failed" if len(errors[key]) else "passed"}
        for key in errors if file_path == key][0]


def format_linter_report(linter_report: dict) -> list:
    return [{"errors": [{
        "line": linter_report[key][i]["line_number"],
        "column": linter_report[key][i]["column_number"],
        "message":linter_report[key][i]["text"],
        "name": linter_report[key][i]["code"],
        "source": "flake8"}
        if len(linter_report[key]) else []
        for i in range(len(linter_report[key]))],
        "path": key,
        "status": "failed" if len(linter_report[key]) else "passed"}
        for key in linter_report]
