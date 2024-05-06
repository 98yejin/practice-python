import os
import hashlib
import logging
import multiprocessing
from tqdm import tqdm
from typing import List, Optional, Tuple
from multiprocessing.pool import AsyncResult

logging.basicConfig(
    filename="file_processing.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
)


def file_processor(file_path: str) -> Tuple[str, Optional[str], Optional[str]]:
    """
    Process a file and calculate its MD5 hash.

    Args:
        file_path (str): The path to the file to be processed.

    Returns:
        Tuple[str, Optional[str], Optional[str]]: A tuple containing the file path, MD5 hash of the file, and any error message encountered during processing.
    """
    try:
        with open(file_path, "rb") as f:
            file_hash = hashlib.md5()
            chunk = f.read(4096)
            while chunk:
                file_hash.update(chunk)
                chunk = f.read(4096)
            return file_path, file_hash.hexdigest(), None
    except Exception as e:
        logging.error(f"Error processing file {file_path}: {e}")
        return file_path, None, str(e)


def process_files(directory: str) -> None:
    """
    Process files in the specified directory using multiprocessing.

    Args:
        directory (str): The directory path containing the files to be processed.

    Returns:
        None
    """
    files = [
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f))
    ]
    pool = multiprocessing.Pool()

    results: List[AsyncResult] = []
    pbar = tqdm(total=len(files), desc="Processing files")

    for file in files:
        result = pool.apply_async(
            file_processor,
            args=(file,),
            error_callback=lambda e: logging.error(f"Error: {e}"),
        )
        results.append(result)

    pool.close()

    for result in results:
        try:
            file_path, hash_digest, error = result.get(timeout=5)
            if error:
                print(f"Error processing {file_path}: {error}")
            else:
                print(f"File: {file_path}, MD5: {hash_digest}")
        except multiprocessing.TimeoutError:
            print(f"Timeout processing file: {file}")
            logging.error(f"Timeout processing file: {file}")
        pbar.update(1)

    pbar.close()
    pool.join()


if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    process_files(directory_path)
