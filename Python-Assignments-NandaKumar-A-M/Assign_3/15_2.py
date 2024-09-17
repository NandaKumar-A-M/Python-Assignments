try:
    file_path = r"C:\Users\nk416\OneDrive\Desktop\errorfile.py"
    with open(file_path, 'r') as file:
        contents = file.read()
        print("File contents:", contents)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except IOError as e:
    print(f"Error: Unable to read file '{file_path}'. {e}")

finally:
    if not file.closed:
        file.close()
