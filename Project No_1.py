import os
import shutil

# The User need to enter the directory path to the Organize
directory = input("Enter The Directory Path Organize: ")

file_types = {
    "jpg": "Images",
    "jpeg": "Images",
    "png": "Images",
    "gif": "Images",
    "bmp": "Images",
    "tiff": "Images",
    "mp4": "Videos",
    "avi": "Videos",
    "mov": "Videos",
    "mkv": "Videos",
    "wmv": "Videos",
    "flv": "Videos",
    "pdf": "Documents",
    "doc": "Documents",
    "docx": "Documents",
    "xls": "Documents",
    "xlsx": "Documents",
    "ppt": "Documents",
    "pptx": "Documents",
    "txt": "Documents",
    "mp3": "Music",
    "aac": "Music",
    "flac": "Music",
    "wav": "Music",
    "ogg": "Music",
    "wma": "Music",
    "": "The Type or Folder isn't exist "

}

# Create folders for each file type if they don't already exist and print the name of folder
for folder in set(file_types.values()):
    folder_path = os.path.join(directory, folder)
    if not os.path.exists(folder_path):
        print(os.path.basename(folder_path))
        os.makedirs(folder_path)

# Screen through all files in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    # check if the file is actually a file (not a directory)
    if os.path.isfile(file_path):
        # get the file extension
        file_extension = filename.split(".")[-1].lower()
        # check if we have a folder for this file type
        if file_extension in file_types:
            # move the file to the corresponding folder
            folder_name = file_types[file_extension]
            folder_path = os.path.join(directory, folder_name)
            shutil.move(file_path, folder_path)
            # Print a message to the user
            print("Files have been organized successfully.")
