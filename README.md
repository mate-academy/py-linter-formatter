 # Linter formatter

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

Линтер flake8 выдает такой отчет об ошибках при проверке каталога с файлами исходного 
кода:
```python
errors = {
    "./test_source_code_2.py": [],
    "./source_code_2.py": [
        {
            "code": "E501",
            "filename": "./source_code_2.py",
            "line_number": 18,
            "column_number": 80,
            "text": "line too long (99 > 79 characters)",
            "physical_line": '    return f"I like to filter, rounding, doubling, '
            "store and decorate numbers: {', '.join(items)}!\"",
        },
        {
            "code": "W292",
            "filename": "./source_code_2.py",
            "line_number": 18,
            "column_number": 100,
            "text": "no newline at end of file",
            "physical_line": '    return f"I like to filter, rounding, doubling, '
            "store and decorate numbers: {', '.join(items)}!\"",
        },
    ],
    "./source_code_1.py": [
        {
            "code": "E702",
            "filename": "./source_code_1.py",
            "line_number": 3,
            "column_number": 74,
            "text": "multiple statements on one line (semicolon)",
            "physical_line": '        new_items = [f"{key} -> {value}" for key, '
            "value in items.items()]; return func(new_items)\n",
        },
        {
            "code": "E501",
            "filename": "./source_code_1.py",
            "line_number": 3,
            "column_number": 80,
            "text": "line too long (97 > 79 characters)",
            "physical_line": '        new_items = [f"{key} -> {value}" for key, '
            "value in items.items()]; return func(new_items)\n",
        },
        {
            "code": "E302",
            "filename": "./source_code_1.py",
            "line_number": 15,
            "column_number": 1,
            "text": "expected 2 blank lines, found 1",
            "physical_line": "def number_filter(func):\n",
        },
        {
            "code": "E303",
            "filename": "./source_code_1.py",
            "line_number": 27,
            "column_number": 1,
            "text": "too many blank lines (6)",
            "physical_line": "@number_filter\n",
        },
        {
            "code": "E501",
            "filename": "./source_code_1.py",
            "line_number": 31,
            "column_number": 80,
            "text": "line too long (99 > 79 characters)",
            "physical_line": '    return f"I like to filter, rounding, doubling, '
            "store and decorate numbers: {', '.join(items)}!\"\n",
        },
    ],
    "./test_source_code_1.py": [
        {
            "code": "E302",
            "filename": "./test_source_code_1.py",
            "line_number": 4,
            "column_number": 1,
            "text": "expected 2 blank lines, found 1",
            "physical_line": "@pytest.mark.parametrize(\n",
        },
        {
            "code": "E501",
            "filename": "./test_source_code_1.py",
            "line_number": 32,
            "column_number": 80,
            "text": "line too long (84 > 79 characters)",
            "physical_line": '            "decorate numbers: 1 -> 2, 2 -> 4, 6 -> 12, -111 -> -222, -50 -> -100!",\n',
        },
        {
            "code": "W292",
            "filename": "./test_source_code_1.py",
            "line_number": 112,
            "column_number": 6,
            "text": "no newline at end of file",
            "physical_line": "    )",
        },
    ],
}
```
Здесь `errors` это словарь, в котором ключи - путь к файлу, а значение этого ключа -
список ошибок, где каждая ошибка - словарь

Но мы храним результаты выполнения немного в другом формате.
Напиши 3 функции, чтобы преобразовать отчет в нужном нам формате.
1. `format_linter_error` - форматирует отдельно взятую ошибку
2. `format_single_linter_file` - форматирует все ошибки для конкретного файла
3. `format_linter_report` - форматирует все ошибки для всех файлов в отчете

Все функции должны вмещать в себе только конструкцию `return`

Требуемый формат хранения:
```python
errors = [
    {"errors": [], "path": "./test_source_code_2.py", "status": "passed"},
    {
        "errors": [
            {
                "line": 18,
                "column": 80,
                "message": "line too long (99 > 79 characters)",
                "name": "E501",
                "source": "flake8",
            },
            {
                "line": 18,
                "column": 100,
                "message": "no newline at end of file",
                "name": "W292",
                "source": "flake8",
            },
        ],
        "path": "./source_code_2.py",
        "status": "failed",
    },
    {
        "errors": [
            {
                "line": 3,
                "column": 74,
                "message": "multiple statements on one line (semicolon)",
                "name": "E702",
                "source": "flake8",
            },
            {
                "line": 3,
                "column": 80,
                "message": "line too long (97 > 79 characters)",
                "name": "E501",
                "source": "flake8",
            },
            {
                "line": 15,
                "column": 1,
                "message": "expected 2 blank lines, found 1",
                "name": "E302",
                "source": "flake8",
            },
            {
                "line": 27,
                "column": 1,
                "message": "too many blank lines (6)",
                "name": "E303",
                "source": "flake8",
            },
            {
                "line": 31,
                "column": 80,
                "message": "line too long (99 > 79 characters)",
                "name": "E501",
                "source": "flake8",
            },
        ],
        "path": "./source_code_1.py",
        "status": "failed",
    },
    {
        "errors": [
            {
                "line": 4,
                "column": 1,
                "message": "expected 2 blank lines, found 1",
                "name": "E302",
                "source": "flake8",
            },
            {
                "line": 32,
                "column": 80,
                "message": "line too long (84 > 79 characters)",
                "name": "E501",
                "source": "flake8",
            },
            {
                "line": 112,
                "column": 6,
                "message": "no newline at end of file",
                "name": "W292",
                "source": "flake8",
            },
        ],
        "path": "./test_source_code_1.py",
        "status": "failed",
    },
]
```