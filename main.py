def format_linter_error(error: dict) -> dict:
    return {'line': error['line'], 'column': error['column'], 'message': error['message']}


