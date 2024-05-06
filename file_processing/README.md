# File Processing Tool

This Python script is designed to process files in a specified directory and calculate their MD5 hashes using multiprocessing. It utilizes the `hashlib` module for computing the MD5 hash and the `multiprocessing` module for parallel processing of files.

## Features

- **File Processing**: The script can process multiple files in a directory and calculate their MD5 hashes.
- **Multiprocessing**: Utilizes multiprocessing to speed up the file processing by utilizing multiple CPU cores.
- **Progress Tracking**: Displays a progress bar using the `tqdm` library to show the status of file processing.
- **Error Handling**: Handles exceptions that may occur during file processing and logs errors to a file.
- **Timeout Handling**: Implements a timeout mechanism to prevent the script from getting stuck on a single file for too long.

## Requirements

- Python 3.x
- Required libraries: `hashlib`, `multiprocessing`, `tqdm`

You can install the required libraries using pip:

```bash

pip install tqdm

```

## Usage

1. Save the script to a file (e.g., `main.py`).
2. Run the script from the command line:

    ```bash

    python main.py

    ```

3. When prompted, enter the directory path containing the files you want to process.

The script will start processing the files in the specified directory and display the file path and MD5 hash for each successfully processed file. If any errors occur during file processing, they will be logged to a file named `file_processing.log` in the same directory.

## Functions

### `file_processor(file_path: str) -> Tuple[str, Optional[str], Optional[str]]`

This function processes a single file and calculates its MD5 hash.

- **Args**:
  - `file_path` (str): The path to the file to be processed.
- **Returns**:
  - Tuple[str, Optional[str], Optional[str]]: A tuple containing the file path, MD5 hash of the file (or `None` if an error occurred), and an error message (or `None` if no error occurred).

### `process_files(directory: str) -> None`

This function processes all files in the specified directory using multiprocessing.

- **Args**:
  - `directory` (str): The directory path containing the files to be processed.
- **Returns**:
  - `None`

## Example Output

```None

Enter the directory path: /path/to/directory
File: /path/to/directory/file1.txt, MD5: d3b07384d113edec49eaa6238ad5ff00
File: /path/to/directory/file2.pdf, MD5: 6a204bd89f3c8348afd5c77c717a097a
Error processing /path/to/directory/file3.txt: [Errno 13] Permission denied: '/path/to/directory/file3.txt'
Timeout processing file: /path/to/directory/file4.zip

```
