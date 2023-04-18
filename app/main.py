def format_linter_error(error: dict) -> dict:

    return {
              type_error: (error[value_error]
              if value_error in error else value_error)
              for type_error, value_error in [
                    ("line", "line_number"),
                    ("column", "column_number"),
                    ("message", "text"),
                    ("name", "code"),
                    ("source", "flake8")
                  ]
            }


def format_single_linter_file(file_path: str, errors: list) -> dict:

    return {
              shared_info: ("passed" if (shared_info == "status" and len(errors) == 0) else info_error)
              for shared_info, info_error in [
                  ("errors", [format_linter_error(error) for error in errors]),
                  ("path", file_path),
                  ("status", "failed")
              ]
            }


def format_linter_report(linter_report: dict) -> list:

    return [format_single_linter_file(file_path, errors) for file_path, errors in linter_report.items()]