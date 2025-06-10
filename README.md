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


