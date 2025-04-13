def format_linter_error(error: dict) -> dict:
    """Formats a single linter error."""
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8",
    }


def format_single_linter_file(file_path: str, errors: list[dict]) -> dict:
    """Formats the linter errors for a single file."""
    formatted_errors = [format_linter_error(error) for error in errors]
    status = "failed" if formatted_errors else "passed"
    return {
        "errors": formatted_errors,
        "path": file_path,
        "status": status,
    }


def format_linter_report(errors: dict) -> list[dict]:
    """Formats the entire linter report."""
    return [
        format_single_linter_file(file_path, errors[file_path])
        for file_path in errors
    ]


def process_data(data: list[int | float]) -> str:
    """Processes some data.

    Returns a success message or raises ValueError if there's an error.
    """
    if not isinstance(data, list):
        raise ValueError("Data must be a list")

    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("Data must contain only numbers")

    if not data:
        raise ValueError("Data list cannot be empty")

    total = sum(data)
    average = total / len(data)

    return f"Processed data: Total={total}, Average={average}"


def greet(name: str) -> str:
    """Greets the person passed in as a parameter"""
    return f"Hello, {name}"


def log_message(message: str) -> None:
    """Logs a message."""
    print(f"Logging: {message}")


def file_process(path: str) -> None:
    """Processes the file under the given path"""
    try:
        with open(path, 'r') as file:
            content = file.read()
            print(f"Processing path: {path}")
            # Process the content here (e.g., parse, analyze, etc.)
            print(f"File content: {content}")  # example
    except FileNotFoundError:
        print(f"Error: File not found at path: {path}")
    except Exception as file_exception:
        print(f"Error processing file: {file_exception}")


if __name__ == "__main__":
    import sys

    try:
        # Simulate reading data from command line arguments
        if len(sys.argv) > 1:
            data_strings = sys.argv[1:]
            input_data = [float(x) for x in data_strings]
        else:
            # Provide default data
            input_data = [1.0, 2.0, 3.0]  # Default data if no arguments are provided

        result = process_data(input_data)
        print(result)
        sys.exit(0)  # Success
    except ValueError as file_exception2:
        print(f"Error: {file_exception2}")
        sys.exit(1)  # Failure
    except Exception as ex:
        print(f"Unexpected error: {ex}")
        sys.exit(1)
