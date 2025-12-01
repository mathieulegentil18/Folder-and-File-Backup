import os
import shutil
from datetime import datetime
import sys

def create_custom_copy(path):
    # Get the current date and time in ISO 8601 (Basic) format
    current_time = datetime.now().strftime('%d %m %Y T%H %M %S')

    # Get the directory and the base name of the file or folder
    directory = os.path.dirname(path)
    base_name = os.path.basename(path)
    
    # Determine if the path is a file or a folder
    if os.path.isfile(path):
        # Get the file extension
        file_name, file_extension = os.path.splitext(base_name)
        # Create the new file name
        new_name = f"{file_name} Backup {current_time}{file_extension}"
        new_path = os.path.join(directory, new_name)
        # Copy the file
        shutil.copy2(path, new_path)
        print(f"Created backup of file: {new_path}")
        
    elif os.path.isdir(path):
        # Create the new folder name
        new_name = f"{base_name} Backup {current_time}"
        new_path = os.path.join(directory, new_name)
        # Copy the folder
        shutil.copytree(path, new_path)
        print(f"Created backup of folder: {new_path}")
        
    else:
        print("The specified path is neither a file nor a directory.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_file_or_folder>")
        sys.exit(1)

    create_custom_copy(sys.argv[1])