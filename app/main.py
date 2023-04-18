def format_linter_error(error: dict) -> dict:
    # write your code here
    code = error.get("code", "")
    filename = error.get("filename", "")
    line_number = error.get("line_number", "")
    column_number = error.get("column_number", "")
    text = error.get("text", "")
    physical_line = error.get("physical_line", "")

    formatted_error = f"Code: {code}\n"
    formatted_error += f"Filename: {filename}\n"
    formatted_error += f"Line number: {line_number}\n"
    formatted_error += f"Column number: {column_number}\n"
    formatted_error += f"Text: {text}\n"
    formatted_error += f"Physical line: {physical_line}\n"
    return formatted_error


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # write your code here
    pass
    formatted_errors = []
    for error in errors:
        formatted_errors.append(format_linter_error(error))

    file_status = "failed" if len(formatted_errors) > 0 else "passed"

    formatted_file = {
        "path": file_path,
        "status": file_status,
        "errors": formatted_errors
    }

    return formatted_file

def format_linter_report(linter_report: dict) -> list:
    # write your code here
    pass
    formatted_report = []
    for file_path, file_errors in errors.items():
        formatted_file = format_single_linter_file(file_path, file_errors)
        formatted_report.append(formatted_file)

    return formatted_report