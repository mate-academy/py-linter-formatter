def format_linter_error(error: dict) -> dict:

    return {"line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:

    return {"errors": [(format_linter_error(errors[i]))
                       for i in range(len(errors))],
            "path": file_path,
            "status": "failed"}


def format_linter_report(linter_report: dict) -> list:

    return [{"errors": [(format_linter_error(linter_report[path][path_in]))
                        for path_in in range(len(linter_report[path]))],
             "path": f"{path}",
             "status": ("passed" if linter_report[path] == [] else "failed")}
            for path, error in linter_report.items()]
