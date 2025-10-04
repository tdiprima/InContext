"""
This demonstrates using ExitStack to dynamically manage multiple contexts (e.g., opening a number of files).
Created temporary sample files for demonstration and read from them inside the stack.
All files are automatically closed after the block, even if exceptions occur.
"""

from contextlib import ExitStack
from pathlib import Path


# Create some temporary sample files for demonstration
def create_sample_files(file_names):
    for name in file_names:
        Path(name).write_text(f"Content of {name}\n")


# Clean up sample files after (optional, for demo)
def cleanup_files(file_names):
    for name in file_names:
        if Path(name).exists():
            Path(name).unlink()


# ExitStack example
if __name__ == "__main__":
    # List of resources (file names)
    resources = ["file1.txt", "file2.txt", "file3.txt"]

    # Create sample files
    create_sample_files(resources)

    print("Starting ExitStack example...")
    with ExitStack() as stack:
        files = []  # To hold file handles
        for res in resources:
            f = stack.enter_context(open(res, "r"))  # Dynamically open and manage
            files.append(f)

        # Now all files are open; read and process them
        for f in files:
            content = f.read().strip()
            print(f"Read from {f.name}: {content}")

    # All files are auto-closed here
    print("ExitStack completed. All files closed.")

    # Clean up
    cleanup_files(resources)
    print("Sample files cleaned up.")
