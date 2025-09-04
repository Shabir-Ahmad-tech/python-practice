# Read the file line by line and convert each line to uppercase

filename = input("Enter the file name (e.g., story.txt): ")

# Ensure the file has .txt extension
if not filename.endswith(".txt"):
    print("Please enter a valid .txt file")
else:
    try:
        with open(filename, "r") as file:   # 'with' automatically closes the file
            for line in file:
                print(line.strip().upper())  # strip removes extra newlines
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")
    except Exception as e:
        print("An error occurred:", e)