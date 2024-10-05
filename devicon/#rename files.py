import os

# Get the current directory
current_directory = os.getcwd()

# Iterate over all files in the current directory
for filename in os.listdir(current_directory):
    # Check if the file name contains "-plain" or "-original"
    if "-plain" in filename or "-original" in filename:
        # Create the new file name by replacing "-plain" and "-original" with an empty string
        new_filename = filename.replace("-plain", "").replace("-original", "")
        # Rename the file
        os.rename(os.path.join(current_directory, filename), os.path.join(current_directory, new_filename))

print("Filenames have been updated.")
