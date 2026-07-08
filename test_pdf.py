from pathlib import Path

from utils.pdf_reader import extract_text_from_pdf


def main():
    project_root = Path(__file__).resolve().parent
    pdf_path = project_root / "data" / "sample.pdf"

    text = extract_text_from_pdf(pdf_path)

    print("Length of extracted text:", len(text))

    if text.strip():
        print(text[:1000])
    else:
        print("No text found in the PDF.")


if __name__ == "__main__":
    main()