def modify_content(content):
    # This function performs a simple modification on the content.
    # Here we convert text to uppercase. You can customize this as needed.
    return content.upper()

def main():
    # Ask the user for the filename.
    filename = input("Enter the filename to read: ")

    try:
        # Open the file in read mode.
        with open(filename, 'r') as infile:
            original_content = infile.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return
    except IOError:
        print(f"Error: The file '{filename}' could not be read.")
        return

    # Modify the content (e.g., convert to uppercase).
    modified_content = modify_content(original_content)

    # Define a new filename for the modified file.
    new_filename = "modified_" + filename

    try:
        # Open the new file in write mode and write the modified content.
        with open(new_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"Modified content has been written to '{new_filename}'.")
    except IOError:
        print(f"Error: Could not write to the file '{new_filename}'.")

if __name__ == "__main__":
    main()
