def read_txt(file_path: str, encoding: str = "utf-8") -> str:
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except UnicodeDecodeError:
        raise UnicodeDecodeError(f"Cannot decode file with {encoding} encoding")
    except Exception as e:
        raise Exception(f"Error reading file: {str(e)}")


def write_txt(*data: str, file_path: str, encoding: str = "utf-8") -> None:
    try:
        with open(file_path, 'w', encoding=encoding) as file:
            for item in data:
                file.write(str(item))
    except PermissionError:
        raise PermissionError(f"No permission to write to file: {file_path}")
    except Exception as e:
        raise Exception(f"Error writing to file: {str(e)}")


def append_txt(*data: str, file_path: str, encoding: str = "utf-8") -> None:
    try:
        with open(file_path, 'a', encoding=encoding) as file:
            for item in data:
                file.write(str(item))
    except PermissionError:
        raise PermissionError(f"No permission to append to file: {file_path}")
    except Exception as e:
        raise Exception(f"Error appending to file: {str(e)}")


if __name__ == '__main__':
    try:
        write_txt("Hello", " World!", file_path="test.txt")
        print("Write test successful")

        content = read_txt("test.txt")
        print(f"Read test successful: {content}")

        append_txt("\nAppended text", file_path="test.txt")
        content = read_txt("test.txt")
        print(f"Append test successful: {content}")

    except Exception as e:
        print(f"Test failed: {str(e)}")
