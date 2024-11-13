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
    template="""Dado el siguiente conjunto de consultas SQL, optimízalas únicamente si se puede mejorar en rendimiento sin cambiar su funcionalidad ni lógica de negocio. 

    Instrucciones detalladas:
    1. **Mantén todas las consultas y estructuras originales**: No elimines ni modifiques ninguna tabla, columna o consulta del conjunto original, y asegúrate de que todas las consultas se retornen en el output, incluyendo *todas* las consultas `SELECT` en el orden en que aparecen en el input.
    
    2. **Preserva la funcionalidad completa de cada consulta**: No alteres los cálculos, condiciones o lógicas, especialmente en el caso de métricas o KPI. La optimización solo debe enfocarse en mejorar la eficiencia sin afectar el resultado lógico.

    3. **Optimiza las uniones**: Identifica y mejora las `JOIN` cuando sea posible, especialmente cuando se trate de `LEFT JOIN` que pueden reducirse a `INNER JOIN` en caso de condiciones de filtro que lo permitan. Evalúa también si se pueden mover condiciones del `WHERE` a las uniones si esto mejora el rendimiento.

    4. **Evita divisiones por cero**: En cualquier cálculo que involucre divisiones, verifica que el divisor no sea cero. Si hay un riesgo de división por cero, utiliza un `CASE WHEN` o `NULLIF` para manejarlo. Por ejemplo, en divisiones como `COUNT(x) / SUM(y)`, reescribe el cálculo como:
    
        ```sql
        COUNT(x) / NULLIF(SUM(y), 0)
        ```

       Esto evitará errores de ejecución cuando el divisor pueda ser cero. Aplica esta lógica en todas las divisiones dentro del conjunto de consultas.

    5. **Uso de COALESCE para valores nulos**: Usa `COALESCE` para asegurar que los valores nulos en agregados no generen resultados inesperados. Por ejemplo, reemplaza valores nulos en sumas y contadores si es necesario:

        ```sql
        COALESCE(SUM(column_name), 0)
        ```

    6. **No omitas consultas adicionales**: Si en el input se incluyen consultas adicionales (como `SELECT * FROM ...` para inspeccionar tablas), asegúrate de que todas aparezcan en el output sin cambios. La respuesta final debe incluir *todas* las consultas del input en el orden original.

    7. **Retorno de la respuesta**: Solo proporciona el código SQL optimizado sin ningún texto adicional ni explicaciones. Si el conjunto de consultas no requiere optimización, responde con: "El Query proporcionado es óptimo".

    Ejemplo de optimización:
    - Si el query original es `SELECT COUNT(a) / SUM(b) FROM table1 WHERE b IS NOT NULL`, asegúrate de reescribirlo para evitar divisiones por cero como `SELECT COUNT(a) / NULLIF(SUM(b), 0) FROM table1 WHERE b IS NOT NULL`.

    Query original: {query}

    Respuesta (SQL únicamente, sin texto adicional ni formatos):
    """,
    input_variables=["query"],
)









    # Initialize the LLM with Llama 3.1 model
    llm = ChatOllama(
        model="llama3.1",
        base_url= "http://ollama-container:11434", 
        verbose=True,
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
    print(text)
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