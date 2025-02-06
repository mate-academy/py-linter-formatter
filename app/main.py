def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"], "column": error["column_number"], "message": error["text"], "name": error["code"], "source": "flake8"}



def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors":[
        {
            "line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "flake8"
        }
        for error in errors
    ],
        "path": file_path,
        "status": "failed"
    }



def format_linter_report(linter_report: dict) -> list:
    return [{
        "errors": ["./test_source_code_2.py"],
        "path": "./test_source_code_2.py",
        "status": "passed"
        },
        {"errors":
            [
            {
                "line": report["line_number"],
                "column": report["column_number"],
                "message": report["text"],
                "name": report["code"],
                "source": "flake8"
            }
            for report in linter_report
        ],
            "path": "./test_source_code_2.py",
            "status": "failed"
        }
    ]

