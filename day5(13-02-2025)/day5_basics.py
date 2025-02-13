# 13-02-2025
with open ("day5_learning.txt","r") as file:
    content=file.read()
    print(content)
    # line = file.readline()
    # while line:
    #   print(line, end='')
    #   line = file.readline()


def read_file_safely(filename):
    """
    Reads the content of a file and prints it.

    Args:
        filename (str): The name of the file to read.
    """
    file = None  # Initialize file object to None
    try:
        file = open(filename, 'r')
        content = file.read()
        print("File Content:\n", content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError as e:
        print(f"Error: An I/O error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if file:
            try:
                file.close()
                print("File closed successfully.")
            except Exception as e:
                print(f"Error closing the file: {e}")

# Example usage:
read_file_safely("test.txt")  # Replace with your filename



def read_file_safely_with(filename):
    """
    Reads the content of a file and prints it using 'with open()'.

    Args:
        filename (str): The name of the file to read.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File Content:\n", content)
            # No need to explicitly close the file; 'with' does it automatically
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError as e:
        print(f"Error: An I/O error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage:
read_file_safely_with("test.txt")  # Replace with your filename


import os

directory_path = "/home/hitesh.jethava@simform.dom/Desktop/Training/Python/day4(12-02-2025)"

if os.path.exists(directory_path):
   print(f"The directory '{directory_path}' exists.")
else:
   print(f"The directory '{directory_path}' does not exist.")