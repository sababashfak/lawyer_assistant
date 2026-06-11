from pathlib import Path
import pymupdf  # This is PyMuPDF


# Current File Directory
CURRENT_DIR = Path(__file__).resolve().parent

# Project Directory
PROJECT_DIR = CURRENT_DIR.parent

# File Directory
FILE_DIR = PROJECT_DIR / "uploads"   #FILE_DIR = PROJECT_DIR / "uploads" / "constitutions"

         
            
# Your target directory
root_dir = Path(FILE_DIR)

for file_path in root_dir.rglob('*'):
    if file_path.is_file():
        print(f"Accessing file: {file_path}")
        
        # Handle PDF files using PyMuPDF
        if file_path.suffix.lower() == '.pdf':
            try:
                # Open the document
                doc = pymupdf.open(file_path)
                content = ""
                
                # Extract text page by page
                for page in doc:
                    text = page.get_text()
                    if text:
                        content += text + "\n"
                
                doc.close()  # Close the file object
                print(f"Successfully read PDF via PyMuPDF. Extracted {len(content)} characters.")
                
            except Exception as e:
                print(f"Error reading PDF {file_path.name}: {e}")
                
        # Handle regular text files
        else:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                print(f"Successfully read text file.")
            except UnicodeDecodeError:
                print(f"Skipping binary/non-text file: {file_path.name}")

