def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "passed" if len(errors) == 0 else "failed"
    }


# Dicionário:
# Key 1 "errors" -> lista com dicionarios passando em format_linter_error (F1)
# Key 2 "path" -> string "file_path" fornecida para a função
# Key 3 "status" -> string indica lista "erros" vazia ("passed") ou ("failed")


def format_linter_report(linter_report: dict) -> list:
    result = []
    for key, errors in linter_report.items():
        result.append(format_single_linter_file(key, errors))

    return result

# Retorna lista contendo:
# 1 -> Dicionário1:
#   Key1 "errors" -> "test_source_code_2.py"
#   Key2 "path" ->
#   Key3 "status"->
#
# 2 -> Dicionário2 contendo erros:
#   Key1 "errors" ->
#   Key2 "path" ->
#   Key3 "status" ->
