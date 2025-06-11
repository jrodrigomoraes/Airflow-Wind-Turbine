# Wind Turbine Simulation with Apache Airflow

This project simulates sensor data from a wind turbine and processes it through an Apache Airflow pipeline. It realistically demonstrates an automated ETL flow with file monitoring, data extraction, parallel branching, database storage, and email notifications based on sensor readings.

---

## Project Overview

The project simulates a wind turbine that generates `.json` files containing sensor data. These files are automatically monitored and processed by an **Apache Airflow DAG**.

The pipeline performs the following steps:

1. Detects when a new JSON file is created.
2. Reads and extracts sensor data from the file.
3. Evaluates the temperature value:
   - If it's **greater than or equal to 24 °C**, sends a **critical alert email**.
   - Otherwise, sends a **normal informational email**.
4. Stores the data in a PostgreSQL database (automatically creates the table if needed).

---

## Technologies Used

- **Python 3.10+**
- **Apache Airflow**
  - FileSensor
  - PythonOperator
  - BranchPythonOperator
  - EmailOperator
  - PostgresOperator
- **PostgreSQL**
- **Docker & Docker Compose**
- **JSON** (for simulated data format)

---

## Project Structure

The project is organized to simulate and process wind turbine sensor data in a structured and automated way. Here's a description of the key components and the order in which they interact:

Data Generation Script, Airflow Directory with dags code and docker-compose.yaml.


---

## Data Generation

Data Generation
The script gerador_dados.py simulates 1000 sensor records from the wind turbine, each including:

idtemp: a unique identifier
powerfactor: power factor
hydraulicpressure: hydraulic pressure
temperature: measured temperature
timestamp: date and time

It saves all records into a data.json file, which is monitored by the Airflow DAG.


---

## Airflow DAG Details

The pipeline defined in `windturbine_dag.py` includes:

1. **FileSensor**  
   Monitors a folder to detect the arrival of new `.json` files.

2. **PythonOperator**  
   Reads the file and pushes its values into XCom variables for downstream use.

3. **Parallel Task Groups:**

   **Group 1: Temperature Evaluation**  
   A `BranchPythonOperator` checks the temperature value.

   Based on the result:  
   - Sends a **critical alert email** if temperature ≥ 24 °C.  
   - Sends a **normal info email** otherwise.

   **Group 2: PostgreSQL Database**  
   - Creates the table `sensors` (if it doesn't exist).  
   - Inserts the sensor data into the table.

---

## Scheduling

The DAG is scheduled to run **every 3 minutes** using:

```python
schedule_interval = '*/3 * * * *
```


## Airflow Configuration

Follow these steps to properly configure your Airflow environment:

### 1. Add a Variable via the Airflow UI

In the Airflow web interface:
```
- Go to **Admin > Variables**
- Click **+** to create a new variable
  - **Key**: `path_file`
  - **Value**: the absolute path of the generated JSON file  
    _Example_: `/opt/airflow/data/data.json`
```

---

### 2. Create a FileSensor Connection

In the Airflow web interface:
```
- Go to **Admin > Connections**
- Click **+ Add**
- Fill in the following:
  - **Conn ID**: `fs_default`
  - **Conn Type**: `File (path)`
  - **Extra**:
    json
    {
      "path": "/opt/airflow/data"
    }

```

---

### 3. Create a PostgreSQL Connection

Still under **Admin > Connections**:
```

- Click **+ Add**
- Fill in the following:
  - **Conn ID**: `postgres`
  - **Conn Type**: `Postgres`
  - Provide the necessary credentials:
    - **Host**
    - **Database**
    - **Username**
```


Email Setup for Alerts
This project uses Airflow's EmailOperator. To make it work, you must configure the SMTP settings in your docker-compose.yaml or airflow.cfg.

Example: Using Gmail SMTP
In your docker-compose.yaml, under both airflow-webserver and airflow-scheduler services, add:
```
AIRFLOW__EMAIL__EMAIL_BACKEND: 'airflow.utils.email.send_email_smtp'
AIRFLOW__SMTP__SMTP_HOST: 'smtp.gmail.com'
AIRFLOW__SMTP__SMTP_PORT: 587
AIRFLOW__SMTP__SMTP_USER: 'your_email@gmail.com'
AIRFLOW__SMTP__SMTP_PASSWORD: 'your_app_password'
AIRFLOW__SMTP__SMTP_MAIL_FROM: 'your_email@gmail.com'

```

 If you're using Gmail, you must enable two-factor authentication and create an App Password to use here.

---

### Expected Result
 Expected Result
- The DAG runs every 3 minutes.

- It detects the new JSON file.

- Extracts and evaluates the sensor data.

- Sends an alert or informational email based on temperature.

- Stores all sensor data in the PostgreSQL database.

**Is this a real simulation of a production pipeline?**  
Yes. This is a practical and realistic simulation of a scheduled data pipeline. It includes real-world components like:

- File monitoring

- Data extraction and branching logic

- Parallel task execution

- Database storage

- Email alerts

- Ideal for practicing ETL development, data engineering, and workflow automation using Airflow.
