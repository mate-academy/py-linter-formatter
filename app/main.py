def format_linter_error(error: dict) -> dict:
    return[
        {
            "line": (error[element][0]["line_number"]),
            "column": (error[element][0]["column_number"]),
            "message": (error[element][0]["text"]),
            "name": (error[element][0]["code"]),
            "source": "flake8"
        }
        for index, element in enumerate(error) if error[element] != []
    ]


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # white your code here
    pass


def format_linter_report(linter_report: dict) -> list:
    # white your code here
    pass
