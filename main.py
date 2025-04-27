def format_linter_error(error):
    return {'line': error['line'], 'column': error['column'], 'message': error['message']}

print(format_linter_error({'line': 42, 'column': 3, 'message': 'Syntax Error'}))