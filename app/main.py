def format_linter_error(error: dict) -> dict:
    return {'column': error["column_number"], 'line': error["line_number"],
            'message': error["text"], 'name': error["code"],
            'source': 'flake8'}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [{'column': error["column_number"],
                        'line': error["line_number"],
                        'message': error["text"],
                        'name': error["code"],
                        'source': 'flake8'} for error in errors],
            'path': file_path, 'status': 'failed'}


def format_linter_report(linter_report: dict) -> list:
    return [{"errors": [{'column': error["column_number"],
                         'line': error["line_number"],
                        'message': error["text"], 'name': error["code"],
                         'source': 'flake8'} for error in linter_report[keys]],
             "path": keys, 'status': ("passed" if len(linter_report[keys]) == 0
            else "failed")} for keys in linter_report]
