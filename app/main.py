def format_linter_report(errors: list[str]) -> str:
    formatted_report = "\n".join(errors)
    return f"Linter Errors:\n{formatted_report}"
