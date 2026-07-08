from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""]
    )

    return text_splitter.split_text(text)


def main():
    sample_text = (
        "PDF chatbots need clean chunks. "
        "This script demonstrates text splitting with overlap."
    )
    chunks = split_text(sample_text)

    print(f"Generated {len(chunks)} chunk(s).")
    for index, chunk in enumerate(chunks, start=1):
        print(f"Chunk {index}: {chunk}")


if __name__ == "__main__":
    main()