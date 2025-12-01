def format_linter_error(error: dict) -> dict:
    return {
        key: value
        for key, value in error.items()
        if key in ('message', 'line', 'column')
    }
    pass


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        key: errors[key]
        for key in ('message', 'line', 'column')
        if key in errors
    }
    pass


def format_linter_report(linter_report: dict) -> list:
    return {
        key: error[key]
        for key in ('message', 'line', 'column')
        if key in error
    }
    pass
