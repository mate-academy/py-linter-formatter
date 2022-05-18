def format_linter_error(error: dict) -> dict:
    res_e = {}
    value_list = []
    for value in error.values():
        value_list.append(value)
    res_e['line'] = value_list[2]
    res_e['column'] = value_list[3]
    res_e['message'] = value_list[4]
    res_e['name'] = value_list[0]
    res_e['source'] = 'flake8'
    return res_e
    pass


def format_single_linter_file(file_path: str, errors: list) -> dict:
    res_single = []
    single = {}
    for error in errors:
        res_single.append(format_linter_error(error))
    single['errors'] = res_single
    single['path'] = file_path
    if not single['errors']:
        single['status'] = 'passed'
    return single
    pass


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file_path, errors)
        for file_path, errors in linter_report.items()
            ]
    pass
