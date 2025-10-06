def read_file(filename):
    """Refactored with proper error handling using with open() and try-except."""
    try:
        with open(filename, "r", encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found")
    except Exception as e:
        raise Exception(f"Error reading file '{filename}': {e}")

# Example usage
if __name__ == "__main__":
    with open("test.txt", "w") as f: f.write("Hello, World!")
    print(read_file("test.txt"))
    try: read_file("nonexistent.txt")
    except FileNotFoundError as e: print(f"Error: {e}")