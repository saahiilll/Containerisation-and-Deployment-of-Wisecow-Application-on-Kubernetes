import subprocess

def backup_directory(source_dir, destination):
    try:
        # Using rsync command to perform the backup
        subprocess.run(['rsync', '-avz', source_dir, destination])
        return "Backup successful!"
    except subprocess.CalledProcessError as e:
        # If rsync encounters an error, it will raise a CalledProcessError
        return f"Backup failed with error: {e}"

if __name__ == "__main__":
    # Input the source directory to be backed up
    source_directory = input("Enter the directory to backup: ")

    # Input the destination directory (remote server or cloud storage)
    destination_directory = input("Enter the destination directory: ")

    # Call the backup_directory function with the specified directories
    result = backup_directory(source_directory, destination_directory)

    # Print the result of the backup operation
    print(result)
