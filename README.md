# Query Optimizer

## Introduction

Optimizing SQL queries is essential for improving the performance of systems that manage large volumes of data, enhancing response times and ensuring the efficient use of resources. However, crafting optimized SQL queries can be a challenging task, particularly as databases grow in complexity and size. As organizations increasingly rely on data for decision-making, it becomes even more crucial to ensure that database queries are efficient and performant. This project was developed to streamline and automate SQL query optimization, leveraging an AI-assisted approach to make the optimization process more accessible and effective for developers, data engineers, and analysts alike.

The SQL Query Optimizer relies on the Llama 3.1 language model, run locally through Ollama, to analyze and enhance the SQL queries. This model is particularly adept at understanding the intricacies of SQL syntax and the underlying logic of the queries, allowing for optimizations that preserve the original intent while improving execution times. By using an intuitive web interface, users can input any SQL query and receive optimized results with a single click, eliminating the need for manual optimization work that can be time-consuming and error-prone. The system processes queries according to pre-configured guidelines that ensure the optimizations improve performance without altering the query’s functionality.

This approach not only automates a traditionally manual process but also provides an effective solution to the growing demand for optimized database performance in environments handling large datasets. The project aims to make SQL query optimization a seamless task, improving overall system efficiency and enabling professionals to focus on higher-level tasks without being bogged down by query performance issues. It serves as a practical, user-friendly tool for businesses that depend heavily on SQL to drive operations and generate insights.

For example, a financial services company analyzing vast amounts of transactional data could greatly benefit from this tool. By optimizing queries used for fraud detection or risk assessment, the system can ensure that these critical operations run efficiently, providing faster insights and reducing system overhead.


## Table of Contents

1. [Structure of repository](#structure-of-repository)
2. [Usage](#usage)
3. [Documentation](#documentation)
4. [Technologies](#technologies)
5. [Collaborators](#collaborators)
6. [License](#license)


## Reference Architecture

## Structure of repository

- ### App ([App](app/)) :
  Folder with the app's python file.
- ### Queries ([Queryes to test](queries/)) :
  Files with list of queries to test the model.
- ### Requirements ([Requirements](requirements)) :
  Text file with the libraries needed to run the model.


## Usage

* Requirements
    - Python 3.10
    - Ollama llama3.1
    - Visual Studio Code
      
* How to start
  1. Clone the repository from GitHub: 
   ```bash
    git clone https://github.com/zavalajb/data-reu-query-optimization.git
    ```
   2. Create a Python environment:
    ```bash
    python -m venv gevenv
    ```

    3. Activate the environment:
    ```bash
    gevenv\Scripts\activate
    ```

    4. Install the requirements:
    ```bash
    pip install -r requirements.txt
    ```
    5. Go to the official Ollama site and download the installer <br><br>
    6. Once the Ollama installer has been executed, we verify that it has been installed correctly with the following command in the CMD: 
    ```bash
    ollama --version
    ```
    7. Once we have verified that it is installed, we download the model that we will use:
    ```bash
    ollama pull llama3.1
    ```
    8. Run the downloaded model with a next command: 
    ```bash
    ollama run llama3.1
    ```
   - Once we have verified that the model is installed correctly, we go to our Visual Studio Code IDE and open the folder that we cloned from our repository.<br><br>

    To run the program, we go to the app folder, and then run it in the terminal of the same Visual Studio Code IDE with the command:
    ```bash
    python app.py
    ```
    - When we run our script, it will connect to port 5000 of our local host, and the URL that we have to open in order to start using our SQL code optimizer will appear in the terminal.        <br><br>
    The URL that we must open is the following:
    ```bash
     http://127.0.0.1:5000
    ```

## Documentation

The SQL Query Optimization model is built around the Llama 3.1 language model from Ollama, which enables effective parsing and improvement of SQL queries. The model operates locally to ensure data privacy and real-time processing, making it an ideal choice for enterprises managing sensitive or large-scale data.

Key components of the application include:

- **Backend and Processing (Python)**: The project is powered by Python, which facilitates the model's integration and execution. The primary application file, app.py, is structured with Flask to launch a local server on port 5000, making the tool easily accessible in a web environment.

- **AI Model (Llama 3.1 via Ollama)**: Llama 3.1 is selected for its language capabilities and adaptability in processing SQL, allowing for nuanced optimizations that enhance performance while preserving query integrity. The model is accessed via Ollama, which enables smooth interaction with the backend.

- **User Interface (HTML and JavaScript)**: A straightforward HTML and JavaScript-based interface enables users to submit queries and view results quickly. This setup ensures a clean, single-click user experience without overwhelming the user with excessive configuration options.

This project’s technology stack was carefully chosen to prioritize local execution, responsiveness, and user-friendly design. By focusing on these areas, the SQL optimizer serves as a robust tool for improving query performance, addressing both speed and simplicity for effective deployment in diverse SQL-dependent environments.


## Technologies
List of the main technologies, programming languages, dependencies, or tools used in the project:
- Python 3.x
- Llama 3.1 (Ollama)
- Flask
- HTML
- JavaScript
- Microsoft SQL Server Management Studio
- Visual Studio Code

## Collaborators

- Berenice Zavala Jiménez (berenice.zavala@axity.com)
- Pedro Daniel Espinosa Nava (pedro.espinosa@Axity.com)


## License

![image](https://github.com/user-attachments/assets/2a29f6f3-a512-458b-a223-bf0484f9bcc3)

### Este ARTE forma parte del CReA de Axity, para más información visitar [CReA]
*[CReA - Inicio (sharepoint.com)](https://intellego365.sharepoint.com/sites/CentralAxity/Corporativo/CReA/SitePages/Home.aspx?xsdata=MDV8MDJ8fGUwYzYzYzgwOGNmZjRjMzIyY2JhMDhkY2UxNjg5ZmU0fDAwYTA1Y2UwYmQzZDQyMTVhNTY5YzYyNjFhMjBhMzllfDB8MHw2Mzg2MzMwODY2NTUxNDcxOTR8VW5rbm93bnxWR1ZoYlhOVFpXTjFjbWwwZVZObGNuWnBZMlY4ZXlKV0lqb2lNQzR3TGpBd01EQWlMQ0pRSWpvaVYybHVNeklpTENKQlRpSTZJazkwYUdWeUlpd2lWMVFpT2pFeGZRPT18MXxMMk5vWVhSekx6RTVPbTFsWlhScGJtZGZUVWRGZWsweVdtbE5hbGwwV2tkS2FFNURNREJOTWxGNlRGUm5kMXBYU1hSTk1rbDNUMVJqZDFsdFVtaE5iVlpxUUhSb2NtVmhaQzUyTWk5dFpYTnpZV2RsY3k4eE56STNOekV4T0RZME56UTB8N2YzMGEyNjYxOTIzNGJkYTJjYmEwOGRjZTE2ODlmZTR8NjE3Y2VhMTRlZDA3NDY3ZGI1OWQxNDdjNGQ0OWY2NGI%3D&sdata=Yk5iaWpjWkoycW13ODdENUI1b05nNTFyRzI2bnlBUkJOZ1RCM0tYUU1QVT0%3D&ovuser=00a05ce0-bd3d-4215-a569-c6261a20a39e%2CPedro.Espinosa%40axity.com&OR=Teams-HL&CT=1727714402558&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiI0OS8yNDA4MTcwMDQyMSIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D)*
    
