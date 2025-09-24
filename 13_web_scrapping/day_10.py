import fitz  # PyMuPDF


def read_pdf(file_path: str) -> str:
    """Read a PDF and return all text as a string."""
    all_text = []

    with fitz.open(file_path) as doc:
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text("text")  # type: ignore
            all_text.append(text)

    return "\n".join(all_text)


if __name__ == "__main__":
    pdf_path = "test.pdf"
    print(read_pdf(pdf_path))
