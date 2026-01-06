def format_linter_error(error: dict) -> dict:
    # write your code here
    return { "line" : error["line"], "column": error["column"], "message": error["message"], "name" : error["name"], "source" : "flake8" }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # write your code here
    results = [format_linter_error(error) for error in errors]
    status = "failed" if len(results) > 0 else "passed"
    return {"errors": results, "path": file_path, "status" : status }
        
    
def format_linter_report(linter_report: dict) -> list:
    # write your code here
    print(linter_report)
    return []
    
