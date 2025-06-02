import fitz  # PyMuPDF
from pdf2image import convert_from_path
from PIL import ImageChops, Image
import difflib
import os

# === User Config ===
suspicious_pdf = ".pdf"
genuine_pdf = ".pdf"
poppler_path = r""  # Change if needed or None

# --- Step 1: Pixel-level difference of first page images ---
def pixel_diff_images(pdf1, pdf2, poppler_path=None):
    suspicious_images = convert_from_path(pdf1, dpi=300, poppler_path=poppler_path)
    genuine_images = convert_from_path(pdf2, dpi=300, poppler_path=poppler_path)
    
    img1 = suspicious_images[0].convert("RGB")
    img2 = genuine_images[0].convert("RGB")
    
    if img1.size != img2.size:
        img2 = img2.resize(img1.size)
    
    diff = ImageChops.difference(img1, img2)
    diff_enhanced = diff.point(lambda p: p * 5)
    
    output_file = "difference_output.png"
    diff_enhanced.save(output_file)
    diff_enhanced.show()
    
    # Save originals for reference
    img1.save("suspicious_page1.png")
    img2.save("genuine_page1.png")
    
    print(f"✅ Pixel diff complete. Diff image saved as '{output_file}'\n")

# --- Step 2: Text extraction and diff ---
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    texts = [page.get_text() for page in doc]
    return "\n".join(texts)

def print_text_diff(text1, text2):
    diff = difflib.unified_diff(
        text1.splitlines(), text2.splitlines(),
        fromfile='Suspicious PDF',
        tofile='Genuine PDF',
        lineterm=''
    )
    print("--- Textual differences ---")
    diff_lines = list(diff)
    if diff_lines:
        for line in diff_lines:
            print(line)
    else:
        print("No textual differences found.")
    print()

# --- Step 3: Metadata comparison ---
def get_pdf_metadata(pdf_path):
    doc = fitz.open(pdf_path)
    return doc.metadata

def print_metadata_diff(meta1, meta2):
    print("--- Metadata differences ---")
    keys = set(meta1.keys()) | set(meta2.keys())
    diff_found = False
    for key in keys:
        val1 = meta1.get(key)
        val2 = meta2.get(key)
        if val1 != val2:
            print(f"{key}: Suspicious = {val1} | Genuine = {val2}")
            diff_found = True
    if not diff_found:
        print("No metadata differences found.")
    print()

# === Main Execution ===
if __name__ == "__main__":
    print("\nStarting PDF comparison...\n")

    # Pixel diff
    pixel_diff_images(suspicious_pdf, genuine_pdf, poppler_path)

    # Text diff
    text_suspicious = extract_text_from_pdf(suspicious_pdf)
    text_genuine = extract_text_from_pdf(genuine_pdf)
    print_text_diff(text_suspicious, text_genuine)

    # Metadata diff
    meta_suspicious = get_pdf_metadata(suspicious_pdf)
    meta_genuine = get_pdf_metadata(genuine_pdf)
    print_metadata_diff(meta_suspicious, meta_genuine)

    print("✅ PDF comparison finished.")
