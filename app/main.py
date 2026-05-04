

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
        "errors": [{
            "line": i["line_number"],
            "column": i["column_number"],
            "message": i["text"],
            "name": i["code"],
            "source": "flake8"
        }for i in errors if i["filename"] == file_path],
        "path": file_path,
        "status": ["failed" if errors else "passed"][0]

    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [
                {
                    "line": j.get("line_number"),
                    "column": j["column_number"],
                    "message": j["text"],
                    "name": j["code"],
                    "source": "flake8"
                }
                for j in i
            ],
            "path": k,
            "status": "failed" if i else "passed"
        }
        for k, i in linter_report.items()
    ]
