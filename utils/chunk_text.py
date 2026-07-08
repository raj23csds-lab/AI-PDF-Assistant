from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(pages, source):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = []

    for page in pages:

        page_chunks = splitter.split_text(page["text"])

        for chunk in page_chunks:

            chunks.append({
                "text": chunk,
                "source": source,
                "page": page["page"]
            })

    return chunks