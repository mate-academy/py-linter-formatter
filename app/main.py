def format_linter_error(error: dict) -> dict:
    return {("line" if error_name == "line_number"
            else "column" if error_name == "column_number"
            else "message" if error_name == "text"
            else "name" if error_name == "code"
            else "source" if error_name == "physical_line"
            else None): ("flake8" if error_name == "physical_line"
            else error_body)
            for (error_name, error_body) in error.items()
            if error_name != "filename"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [{("line" if error_name == "line_number"
            else "column" if error_name == "column_number"
            else "message" if error_name == "text"
            else "name" if error_name == "code"
            else "source" if error_name == "physical_line"
            else None): ("flake8" if error_name == "physical_line"
            else error_body)
            for (error_name, error_body) in error.items()
            if error_name != "filename"} for error in errors],
            "paths": file_path,
            "status": ("failed" if len(errors) > 0 else "passed")}


def format_linter_report(linter_report: dict) -> list:
    return [
        {"errors": [{("line" if error_name == "line_number"
                    else "column" if error_name == "column_number"
                    else "message" if error_name == "text"
                    else "name" if error_name == "code"
                    else "source"): ("flake8" if error_name == "physical_line"
                    else error_body)
                    for (error_name, error_body) in error.items()
                    if error_name != "store and decorate numbers:"}
                    for error in list_of_errors],
         "path": path_to_file,
         "status": ("failed" if len(list_of_errors) > 0 else "passed")}
        for (path_to_file, list_of_errors) in linter_report.items()]
