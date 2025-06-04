# Data-Quality-Monitoring-System-using-Python-Pandas
Automated Data Quality Monitoring System – Python-based project to detect missing values, schema issues, and data inconsistencies in CSV datasets. Ideal for data pipelines and engineering workflows.
This project is a lightweight, customizable data quality monitoring system built with Python and Pandas. It validates datasets by checking for missing values, schema mismatches, duplicate records, and more. Ideal for data engineers, analysts, and teams enforcing clean data pipelines before using it for analytics or machine learning.

✅ Features
🔍 Automated Data Validation
Validates datasets for missing values, duplicates, schema mismatches, and custom business rules.

🧠 Configurable Rule Engine
Easily define and manage validation rules via YAML/JSON or directly in code.

📉 Data Profiling Dashboard (Optional)
Summary stats including null counts, distinct values, types, and value ranges for QA reports.

🔔 Alerting System
Sends alerts via email/console when data quality checks fail (can be extended to Slack or monitoring tools).

🗂️ Modular Code Structure
Ready to be integrated with ETL pipelines or CI/CD workflows.

⚙️ Tech Stack
Python 3.12
Pandas
YAML / JSON
(Optional: Great Expectations / PyDeequ / Airflow / Streamlit)

📁 Sample Checks Performed
Check Type	Description
Missing Values	Ensures no NULLs in critical columns
Uniqueness	Primary keys must be unique
Range Checks	Values fall within expected thresholds
Regex Validation	Format checking for emails, IDs, etc.
Schema Validation	Column names, types, and order check

🧪 Sample Dataset
Includes a sample titanic.csv dataset and rules_config.yaml to demonstrate live checks.

🚀 How to Run
[bash]
# Step 1: Clone the repo
git clone https://github.com/Sakshi26-aftk/data-quality-monitoring.git
cd data-quality-monitoring

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Run the checker
python app.py


🛠 Future Scope
Integration with Apache Airflow DAGs
Visualization of check results via Streamlit
Auto-logging into PostgreSQL/MongoDB
Data Drift Detection using statistical tests

📌 Use Case
This system is ideal for:
Data Engineers maintaining pipeline health
Analysts who depend on clean data
Organizations enforcing data governance policies

