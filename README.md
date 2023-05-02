
# Streamlit_Auto_Spare_Management_System
This project aims to build a Spare Part Management System using Streamlit as frontend and Mariadb mysql for backend.


## Installation

Install python libraries with pip/pip3
 - lib_name:
    - mysql-connector
    - streamlit

```bash
  pip install <lib_name>
```
    
## Deployment
Before running the application, setup the mysql database
- create database named *spare_parts_project*
- import *db_crt.sql* into mysql
- **database shouldn't have password**
    - If it has password, then mention it in *app.py* file mysql-connector as parameter

To deploy this project run

```bash
  run app.py
```

## SreenShots
![image](https://user-images.githubusercontent.com/79711475/235580811-5a85b3c9-682e-47dc-a066-e023aef8fb80.png)
![image](https://user-images.githubusercontent.com/79711475/235580840-357d9c13-d742-4f9f-b7e0-9ea6543bdbbd.png)
![image](https://user-images.githubusercontent.com/79711475/235580874-ef6ab34f-2e94-4b72-bafb-c5bfe1cd7e97.png)
![image](https://user-images.githubusercontent.com/79711475/235580910-d5f8db14-4dff-4237-a3f2-7a5b93d9e342.png)
![image](https://user-images.githubusercontent.com/79711475/235580957-c08b5440-55b3-455a-9781-698f52f893c1.png)




