def format_linter_error(error: dict) -> dict:

    return {                                   #Спомощью ключей выбираем нужные нам елементы 
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }
    
def format_single_linter_file(file_path: str, errors: list) -> dict:
    
    return {
        "errors": [format_linter_error(error) for error in errors], #Мы проходимся по функции несколько раз
        "path": file_path,
        "status": "failed" if errors else "passed" #Делаем проверку 
    }

def format_linter_report(linter_report: dict) -> list:

    return [ 
        format_single_linter_file(path, errors) 
        for errors, path in linter_report.items()
    ]