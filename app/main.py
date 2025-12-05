def format_linter_error(error: dict) -> dict:
    """
    Formata um erro individual do linter.

    Args:
        error: Dicionário contendo informações do erro

    Returns:
        Dicionário formatado com as chaves: line, column, text, name, code
    """
    return {
        "line": error.get("line_number", error.get("line", 0)),
        "column": error.get("column_number", error.get("column", 0)),
        "text": error.get("text", error.get("message", "")),
        "name": error.get("code", error.get("error_name", "")),
        "code": error.get("code", error.get("error_code", ""))
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    """
    Formata todos os erros de um único arquivo.

    Args:
        file_path: Caminho do arquivo
        errors: Lista de erros do linter para este arquivo

    Returns:
        Dicionário formatado com as chaves: errors e file_path
    """
    formatted_errors = [format_linter_error(error) for error in errors]

    return {
        "errors": formatted_errors,
        "file_path": file_path
    }


def format_linter_report(linter_report: dict) -> list:
    """
    Formata um relatório completo do linter.

    Args:
        linter_report: Dicionário contendo o relatório do linter,
                      onde as chaves são caminhos de arquivos e
                      os valores são listas de erros.

    Returns:
        Lista de dicionários formatados, um para cada arquivo
    """
    result = []

    for file_path, errors in linter_report.items():
        if errors:  # Só inclui arquivos que têm erros
            formatted_file = format_single_linter_file(file_path, errors)
            result.append(formatted_file)

    return result


# Exemplo de uso:
if __name__ == "__main__":
    # Exemplo de entrada
    sample_errors = [
        {
            "line_number": 5,
            "column_number": 10,
            "text": "Trailing whitespace",
            "code": "W291"
        },
        {
            "line": 8,
            "column": 3,
            "message": "Missing whitespace after ','",
            "error_code": "C0326"
        }
    ]

    # Teste format_linter_error
    print("Formatted single error:")
    print(format_linter_error(sample_errors[0]))
    print()

    # Teste format_single_linter_file
    print("Formatted file errors:")
    print(format_single_linter_file("test.py", sample_errors))
    print()

    # Teste format_linter_report
    sample_report = {
        "file1.py": [
            {"line": 1, "column": 1, "message": "Syntax error", "code": "E001"}
        ],
        "file2.py": [],
        "file3.py": [
            {"line": 10, "column": 5, "message": "Line too long", "code": "C0301"},
            {"line": 15, "column": 2, "message": "Undefined variable", "code": "E0602"}
        ]
    }

    print("Formatted linter report:")
    formatted_report = format_linter_report(sample_report)
    for file_report in formatted_report:
        print(file_report)