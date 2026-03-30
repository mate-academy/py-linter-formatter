def get_users_data(users_list):
    return {user_id: {"username": username, "email": email, "password": password} for user_id, username, email, password in users_list}


def format_linter_error(error):
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path, errors):
    return {
        "errors": [format_linter_error(e) for e in errors],
        "path": file_path,
        "status": "passed" if not errors else "failed"
    }


def format_linter_report(linter_report):
    return [format_single_linter_file(file_path, errors) for file_path, errors in linter_report.items()]
