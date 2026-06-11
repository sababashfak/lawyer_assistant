import pymupdf
from pathlib import Path
# pip install langchain-community
# pip install -U langchain-community pypdf
# pip install "unstructured[pdf]

#from langchain_community.document_loaders import DirectoryLoader

# Current File Directory
CURRENT_DIR = Path(__file__).resolve().parent

# Project Directory
PROJECT_DIR = CURRENT_DIR.parent

# File Directory
FILE_DIR = PROJECT_DIR / "uploads" / "constitutions"

#print(FILE_DIR)


# loader = DirectoryLoader(FILE_DIR, glob="**/*.*")
# docs = loader.load()

# print(docs)



from pathlib import Path

# Define the root folder you want to scan
root_dir = Path("your_folder_path")

# '*' matches all files and subfolders recursively
for file_path in root_dir.rglob('*'):
    # Check if the path points to an actual file rather than a folder
    if file_path.is_file():
        print(f"Accessing file: {file_path}")
        
        # Access or read the file directly
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()






#doc = 



print("Success")