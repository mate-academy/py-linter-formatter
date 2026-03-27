def format_linter_error(error: dict) -> dict:

    return {new_key: error[old_key]
            for old_key, new_key in
            [("line_number", "line"),
             ("column_number", "column"),
             ("text", "message"),
             ("code", "name")]
            if old_key in error} | {"source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:

    return {
        "errors":
        [{new_key: dc[old_key]
            for old_key, new_key in
            [("line_number", "line"),
             ("column_number", "column"),
             ("text", "message"),
             ("code", "name")]
            if old_key in dc} | {"source": "flake8"}
         for dc in errors
         if dc["filename"] == file_path],
        "path": file_path, "status": "failed" if errors else "passed"}


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [] if not value else [{
                new_key: dc[old_key]
                for old_key, new_key in
                [("line_number", "line"),
                 ("column_number", "column"),
                 ("text", "message"),
                 ("code", "name")]
                if old_key in dc
            } | {"source": "flake8"} for dc in value],
            "path": key,
            "status": "passed" if len(value) == 0 else "failed"

        } for key, value in linter_report.items()
    ]
