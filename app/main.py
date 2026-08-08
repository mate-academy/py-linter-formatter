
def format_linter_error(error: dict) -> dict:
    """
    format_linter_error - formats a single error
    :param error:
    :return: formatted error
    """
    return {"line" : error["line_number"],
            "column" : error["column_number"],
            "message" : error["text"],
            "name" : error["code"], "source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    """
    format_single_linter_file - formats a single linter file
    :param file_path:
    :param errors:
    :return: formatted linter file
    """
    return {"errors": [format_linter_error(error) for error in errors],
            "path" : file_path,
            "status": "passed" if len(errors) == 0 else "failed"}


def format_linter_report(linter_report: dict) -> list:
    """
    format_linter_report - formats a linter report
    :param linter_report:
    :return: formatted linter report
    """
    return [format_single_linter_file(file, file_report)
            for file, file_report in linter_report.items()]
