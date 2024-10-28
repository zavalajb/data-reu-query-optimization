from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# Define the prompt template for the LLM



# Define the RAG application class
class OptmApplication:
    def __init__(self, optimize_chain):
        self.optimize_chain = optimize_chain
    def run(self, question):
        # Retrieve relevant documents
        # Extract content from retrieved documents
        # Get the answer from the language model
        answer = self.optimize_chain.invoke({"question": question})
        return answer
    

prompt = PromptTemplate(
    template="""Based on your data bases kwnoledge answer the question:
    Question: {question}

    Answer:
    """,
    input_variables=["question"],# "documents"],
)


# Initialize the LLM with Llama 3.1 model
llm = ChatOllama(
    model="llama3.1",
    temperature=0,
)


# Create a chain combining the prompt template and LLM
optimize_chain = prompt | llm | StrOutputParser()
optm_application = OptmApplication(rag_chain=optimize_chain)

file = """SELECT * FROM employees e 
WHERE e.department_id IN (SELECT department_id FROM departments WHERE location_id = 1700)"""

question = f"""Could you split in sql statements the content of this file {file}"""
answer = optm_application.run(question)
print("Question:", question)
print("Answer:", answer)

