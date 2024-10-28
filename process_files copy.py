import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import logging
from langchain_community.document_loaders import TextLoader, PyPDFLoader, UnstructuredCSVLoader, UnstructuredExcelLoader , UnstructuredHTMLLoader, UnstructuredMarkdownLoader,UnstructuredPowerPointLoader,UnstructuredWordDocumentLoader#AzureAIDocumentIntelligenceLoader#, MarkdownLoader, PowerPointLoader, DocxLoader, HTMLLoader, HTMLLoader,
import yaml

from langchain_community.vectorstores import SKLearnVectorStore


from langchain_ollama import ChatOllama

def load_files(path = "queries/test.sql"):
        """
        Split documents into smaller chunks for processing and then add the list of chunked 
        documents to a chroma database using an embedding from HuggingFaceEmbeddings.
        
        :param path: Path to the directory containing the documents.
        """
        loaders = {
            '.txt': TextLoader,
            '.pdf': PyPDFLoader,
            '.docx': UnstructuredWordDocumentLoader,
            '.html': UnstructuredHTMLLoader,
            '.csv': UnstructuredCSVLoader,
            '.json': UnstructuredHTMLLoader,
            '.md': UnstructuredMarkdownLoader,
            '.pptx': UnstructuredPowerPointLoader,
            '.xlsx': UnstructuredExcelLoader
        }
        
        
        file = open(path)
        file = file.read()     
        queries = []
        for line in file:
             line = line.strip()
        return file.split("SELECT")


#print(load_files( "./queries", chunk_size=10, chunk_overlap=0))



vectorstore = SKLearnVectorStore.from_documents(
    documents=load_files( "./queries", chunk_size=10, chunk_overlap=0),
    embedding=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"),
)

retriever = vectorstore.as_retriever(k=1) # k=4

from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# Define the prompt template for the LLM
prompt = PromptTemplate(
    template="""Based on your data bases kwnoledge answer the question:
    Question: {question}

    Answer:
    """,
    input_variables=["question"],# "documents"],
)
# Documents: {documents}


# Initialize the LLM with Llama 3.1 model
llm = ChatOllama(
    model="llama3.1",
    temperature=0,
)


# Create a chain combining the prompt template and LLM
rag_chain = prompt | llm | StrOutputParser()


# Define the RAG application class
class RAGApplication:
    def __init__(self, retriever, rag_chain):
        self.retriever = retriever
        self.rag_chain = rag_chain
    def run(self, question):
        # Retrieve relevant documents
        documents = self.retriever.invoke(question)
        # Extract content from retrieved documents
        doc_texts = "\\n".join([doc.page_content for doc in documents])
        # Get the answer from the language model
        answer = self.rag_chain.invoke({"question": question, "documents": doc_texts})
        return answer

#print(file)
# Initialize the RAG application
rag_application = RAGApplication(retriever, rag_chain)
# Example usage
#question = """Could you help me to optimize this query SELECT * FROM employees e 
#WHERE e.department_id IN (SELECT department_id FROM departments WHERE location_id = 1700)"""
#answer = rag_application.run(question)
#print("Question:", question)
#print("Answer:", answer)


question = f"""Could you split in sql statements the content of this file {file}"""
answer = rag_application.run(question)
print("Question:", question)
print("Answer:", answer)