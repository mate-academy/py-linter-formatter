def format_linter_error(error: dict) -> dict:
    return {'line': error['line_number'],
            'column': error['column_number'],
            'message': error['text'],
            'name': error['code'],
            'source': 'flake8'
            }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {'errors': [{'line': errors[i]['line_number'],
                        'column': errors[i]['column_number'],
                        'message': errors[i]['text'],
                        'name': errors[i]['code'],
                        'source': 'flake8'
                        } for i in range(len(errors))],
            'path': file_path, 'status': 'failed'}


def format_linter_report(linter_report: dict) -> list:
    return [{'errors': [{'line': j['line_number'],
                         'column': j['column_number'],
                         'message': j['text'],
                         'name': j['code'],
                         'source': 'flake8'
                         } for j in values], 'path': keys, 'status': 'failed'}
            if linter_report[keys] != [] else
            {'errors': [], 'path': keys, 'status': 'passed'}
            for keys, values in linter_report.items()]
