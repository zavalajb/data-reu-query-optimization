## Usage
* Requirements
    - Python 3.10
      
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





    
