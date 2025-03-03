import pytest
import ast
import inspect

from app import main
from app.main import (
    format_linter_error,
    format_single_linter_file,
    format_linter_report,
)

@pytest.mark.parametrize(
    "error_linter,error_mate",
    [
        (
            {
                "code": "E501",
                "filename": "./source_code_2.py",
                "line_number": 18,
                "column_number": 80,
                "text": "line too long (99 > 79 characters)",
                "physical_line": "    return f\"I like to filter, rounding, doubling, "
                                 "store and decorate numbers: {', '.join(items)}!\"",
            },
            {
                "line": 18,
                "column": 80,
                "message": "line too long (99 > 79 characters)",
                "name": "E501",
                "source": "flake8",
            },
        )
    ],
)
def test_format_linter_error(error_linter, error_mate):
    assert format_linter_error(error_linter) == error_mate, (
        f"Function 'format_linter_error' should return {error_mate}, "
        f"when 'error' equals {error_linter}"
    )

@pytest.mark.parametrize(
    "func",
    [
        format_linter_error,
        format_single_linter_file,
        format_linter_report,
    ],
)
def test_format_functions_one_line(func):
    code = inspect.getsource(func)
    assert (
        isinstance(ast.parse(code).body[0].body[0], ast.Return) is True
    ), f"Function '{func.__name__}' should contain only return statement"

@pytest.mark.parametrize(
    "file_path,errors,result",
    [
        (
            "./source_code_2.py",
            [
                {
                    "code": "E501",
                    "filename": "./source_code_2.py",
                    "line_number": 18,
                    "column_number": 80,
                    "text": "line too long (99 > 79 characters)",
                    "physical_line": "    return f\"I like to filter, rounding, doubling, "
                                     "store and decorate numbers: {', '.join(items)}!\"",
                }
            ],
            {
                "errors": [
                    {
                        "line": 18,
                        "column": 80,
                        "message": "line too long (99 > 79 characters)",
                        "name": "E501",
                        "source": "flake8",
                    }
                ],
                "path": "./source_code_2.py",
                "status": "failed",
            },
        )
    ],
)
def test_format_single_linter_file(file_path, errors, result):
    assert format_single_linter_file(file_path, errors) == result, (
        f"Function 'format_single_linter_file' should return {result}, "
        f"when 'file_path' equals {file_path}, and 'errors' equals {errors}"
    )

def test_comment_deleted():
    lines = inspect.getsource(main)
    assert "# write your code here" not in lines, (
        "Remove the unnecessary comment '# write your code here'"
    )

def test_double_quotes_instead_of_single():
    lines = inspect.getsource(main)
    assert "'" not in lines, (
        'You have to use double quotes "" instead of single quotes \'\''
    )
