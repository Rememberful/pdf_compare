# pdf_compare
This tool helps to identify any fraud train tickets (IRCTC railway tickets)

# PDF Comparison Tool 📄🔍

This Python script offers a comprehensive way to compare two PDF files. It meticulously analyzes and reports differences in three key areas: pixel-level discrepancies on the first page, variations in textual content across all pages, and inconsistencies in metadata.

---

## ✨ Features

* **Visual Pixel Comparison**: Converts the first page of each PDF into an image and highlights any pixel-level differences, saving the result as an image file.
* **Textual Difference Analysis**: Extracts text from all pages of both PDFs and presents a comparison using a unified diff format, making it easy to spot changes.
* **Metadata Discrepancy Report**: Fetches and compares metadata fields from both PDF files, reporting any variations found.

---

## ⚙️ Requirements

To run this script, you'll need:

* Python 3.7 or newer
* The following Python libraries:
    * [PyMuPDF (fitz)](https://pypi.org/project/PyMuPDF/)
    * [pdf2image](https://pypi.org/project/pdf2image/)
    * [Pillow (PIL)](https://pypi.org/project/Pillow/)
* **Poppler**: This is a PDF rendering library required by `pdf2image`.

---

## 🛠️ Installation

1.  **Install Python Dependencies**:
    Open your terminal or command prompt and run:
    ```bash
    pip install pymupdf pdf2image pillow
    ```

2.  **Install Poppler**:
    The installation method for Poppler varies by operating system:
    * **Windows**:
        1.  Download the latest Poppler binaries from a source like [this Poppler for Windows GitHub page](https://github.com/oschwartz10612/poppler-windows/releases/).
        2.  Extract the archive to a location on your computer (e.g., `C:\Program Files\poppler-0.68.0_x86_64`).
        3.  You will need to note the path to the `bin` folder within the extracted Poppler directory (e.g., `C:\Program Files\poppler-0.68.0_x86_64\bin`).
    * **Linux** (Debian/Ubuntu based):
        ```bash
        sudo apt update
        sudo apt install poppler-utils
        ```
    * **MacOS** (using Homebrew):
        ```bash
        brew install poppler
        ```

---

## 🔧 Configuration

Before running the script, you need to specify the paths to your PDF files and, if you're on Windows and haven't added Poppler to your system's PATH, the path to the Poppler `bin` directory.

Edit the script (`pdf_compare.py` or your script's name) and update these lines:


## Set the paths to the two PDFs you want to compare
suspicious_pdf = "path/to/your/suspicious.pdf"
genuine_pdf = "path/to/your/genuine.pdf"

## Set the Poppler path if needed (primarily for Windows if not in PATH)
## Example for Windows: poppler_path = r"C:\Program Files\poppler-0.68.0_x86_64\bin"
## For Linux/MacOS or if Poppler is in PATH on Windows, set to None
poppler_path = None

* Replace `"path/to/your/suspicious.pdf"` and `"path/to/your/genuine.pdf"` with the actual file paths to the PDFs you wish to compare.
* If you are on **Windows** and Poppler is not added to your system's PATH, update `poppler_path` with the correct path to the Poppler `bin` folder (e.g., `r"C:\path\to\poppler\bin"`).
* If Poppler is in your system PATH (common on Linux/MacOS, or if manually added on Windows), you can leave `poppler_path` as `None`.

---

## 🚀 Usage

Once the requirements are installed and the script is configured:

1.  Navigate to the directory where you saved the script using your terminal or command prompt.
2.  Run the script using Python:
    ```bash
    python pdf_compare.py
    ```

The script will then execute the comparison and:

* Generate and display an image file named `difference_output.png` showing the visual differences between the first pages of the two PDFs.
* Print the textual differences found between the PDFs to the console.
* Print any metadata differences found between the PDFs to the console.

---

## 📊 Output

* **`difference_output.png`**: An image file saved in the same directory as the script. This image visually highlights the pixel-level differences detected on the first page of the compared PDFs.
* **Console Output**:
    * **Textual Differences**: Presented in a unified diff format directly in your terminal.
    * **Metadata Differences**: Listed field by field in your terminal.

---

## 📝 Notes

* Pixel comparison is limited to the **first page** of each PDF to manage processing time and complexity.
* Textual content and metadata are extracted and compared for **all pages** within the PDFs.
* Ensure that the PDF files you are comparing are accessible by the script and are **not password-protected**, as this may interfere with the extraction processes.

---

## 📜 License

This script is provided "as-is" without any warranty. You are free to use, modify, and distribute it as you see fit.
