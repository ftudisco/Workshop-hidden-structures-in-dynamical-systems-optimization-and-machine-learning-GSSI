import os

def rename_files_to_lowercase():
    """Recursively rename all files in current directory and subdirectories to lowercase."""
    for root, dirs, files in os.walk('.'):
        # Rename files
        for filename in files:
            old_path = os.path.join(root, filename)
            new_path = os.path.join(root, filename.lower())
            if old_path != new_path:
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed: {old_path} -> {new_path}")
                except OSError as e:
                    print(f"Error renaming {old_path}: {e}")
        
        # Rename directories
        for dirname in dirs:
            old_path = os.path.join(root, dirname)
            new_path = os.path.join(root, dirname.lower())
            if old_path != new_path:
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed directory: {old_path} -> {new_path}")
                except OSError as e:
                    print(f"Error renaming directory {old_path}: {e}")

if __name__ == "__main__":
    rename_files_to_lowercase()

