from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader


# Extract Data From the PDF File
def load_pdf_file(path):
    loader = DirectoryLoader(path,
                             glob="*.pdf",
                             loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents


# Split the data into text chunks
def text_split(extract_data):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=10)
    text_chunks = splitter.split_documents(extract_data)
    return text_chunks


# Download the embedding model from Hugging Face
def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return embeddings
