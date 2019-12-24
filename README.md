# BigProject-DataRep


## Building the project:

The first step was to develop the environment with Flask.  
Then server.  
Then build the CRUD.  
Launch to a web page.  

### Requirements:  

In the cmder create virtual environment:  

* install python -m venv venv   
*  venv\Scripts\activate.bat    
*  pip freeze  
* pip freeze>requirements.txt  
* pip install flash  
* set FLASH_APP (=server name)  

### Add ins
* pip install flash mysql.connector (allows mariadb and studio code and html interact with the databases.)
    this came installed with wampserver.


The following commands can be ran in cmder to run the programme:

* python server1.py or   
* flask run(this was the preferred)

The Following was outputted:
C:\Users\Owner\Desktop\project
(venv) λ flask run
 * Serving Flask app "server1"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 
