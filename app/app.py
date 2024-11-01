from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
#API related packages
from flask import Flask, request, jsonify, render_template, send_from_directory

from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS, cross_origin
# Define the prompt template for the LLM

#Logging
import logging
import json

# Define the RAG application class
class OptmApplication:
    def __init__(self, optimize_chain):
        self.optimize_chain = optimize_chain
    def run(self, query):
        # Retrieve relevant documents
        # Extract content from retrieved documents
        # Get the answer from the language model
        answer = self.optimize_chain.invoke({"query": query})
        cleaned_answer = answer.replace("```sql", "").replace("```", "").replace("\n", " ").replace("\\n", " ").strip()
        cleaned_answer = ' '.join(cleaned_answer.split())
        return cleaned_answer
    
def init():
    global prompt 
    global llm
    global optimize_chain
    global optm_application 
    prompt = PromptTemplate(
        template="""Given the following SQL query, provide an optimized SQL query only, without any additional text:
        
        Original Query: {query}
        
        Optimized Query (SQL only, no additional text or formatting):
        """,
        input_variables=["query"],# "documents"],
    )


    # Initialize the LLM with Llama 3.1 model
    llm = ChatOllama(
        model="llama3.1",
        temperature=0,
    )
    logger.info("llama3.1 model loaded successfully")

    # Create a chain combining the prompt template and LLM
    optimize_chain = prompt | llm | StrOutputParser()
    optm_application = OptmApplication(optimize_chain=optimize_chain)



app = Flask(__name__)
#Cors configuration
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "OPTIONS"]}})
logger = app.logger

logger.info("Initializing app")
init()
logger.info("Initialized app")


@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

@app.route('/')
def home():
    return render_template('index.html')

#@app.route('/main.js')
#def serve_js():
#    return send_from_directory(template_dir, 'main.js')

@app.route('/optimization', methods=['POST'])
def optimization():
    text = request.form.get('text')
    if text is None:
        return jsonify({"error": "Missing 'text' parameter"}), 400
    
    query = text
    try:
        logger.info("Optimizing query")
        answer = optm_application.run(query)
        logger.info("Query optimized")
        return jsonify({"result": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)