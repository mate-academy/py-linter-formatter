def format_linter_error(error: dict) -> dict:
    
    return {
        change_name_dict[key]: (error[key] if key in error.keys() else key) 
        for key in change_name_dict.keys()
    }

change_name_dict = {
    "line_number": "line",
    "column_number": "column",
    "text": "message",
    "code": "name",
    "flake8": "source"
}

def format_single_linter_file(file_path: str, errors: list) -> dict:
    
    return {"errors": [], "path": file_path, "status": "passed"} if errors == [] else {"errors": [format_linter_error(error) for error in errors],
    "path": file_path, "status": "failed"}


def format_linter_report(linter_report: dict) -> list:
    
    return list(
        format_single_linter_file(file_path, errors)
        for file_path, errors in linter_report.items()
    )
        

