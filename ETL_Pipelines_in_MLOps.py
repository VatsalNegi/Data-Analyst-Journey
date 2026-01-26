"""
Create_ETL_Pipelines_in_MLOps.py
--------------------------------

Topic: ETL Pipelines in MLOps
Author: Vatsal Negi
Purpose:
    - Understand ETL (Extract, Transform, Load) in MLOps
    - Learn how data flows from source to storage
    - Build a simple ETL pipeline using Python
    - Prepare foundation for Airflow, Feature Store & Model Training

ETL is the backbone of MLOps pipelines.
"""

# =====================================================
# 1. WHAT IS ETL IN MLOPS?
# =====================================================
"""
ETL stands for:
    E - Extract   → Get data from sources
    T - Transform → Clean, process, feature engineer
    L - Load      → Store data for ML models

In MLOps, ETL helps:
    - Keep data consistent
    - Automate data pipelines
    - Enable reproducible ML experiments
"""

# =====================================================
# 2. DATA SOURCES (EXTRACT)
# =====================================================
"""
Common Data Sources:
    - CSV / Excel files
    - Databases (SQL / NoSQL)
    - APIs
    - Logs
    - Cloud Storage (S3, GCS)

Here we simulate data extraction from a CSV file
"""

import pandas as pd

def extract_data(file_path):
    """
    Extract data from CSV file
    """
    print("Extracting data...")
    data = pd.read_csv(file_path)
    return data


# =====================================================
# 3. DATA TRANSFORMATION
# =====================================================
"""
Transformation includes:
    - Removing null values
    - Encoding categorical features
    - Feature scaling
    - Data validation
"""

def transform_data(df):
    """
    Transform the extracted data
    """
    print("Transforming data...")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing values
    df = df.fillna(0)

    # Example feature engineering
    if 'salary' in df.columns:
        df['salary_in_lakhs'] = df['salary'] / 100000

    return df


# =====================================================
# 4. DATA STORAGE (LOAD)
# =====================================================
"""
Where data is stored after ETL:
    - Data Warehouse (structured data)
    - Data Lake (raw + processed data)
    - Object Storage (S3, GCS)
"""

def load_data(df, output_path):
    """
    Load transformed data into storage
    """
    print("Loading data...")
    df.to_csv(output_path, index=False)
    print("Data successfully loaded!")


# =====================================================
# 5. COMPLETE ETL PIPELINE
# =====================================================
def etl_pipeline(input_path, output_path):
    """
    End-to-end ETL pipeline
    """
    data = extract_data(input_path)
    transformed_data = transform_data(data)
    load_data(transformed_data, output_path)


# =====================================================
# 6. PIPELINE EXECUTION
# =====================================================
if __name__ == "__main__":
    input_file = "raw_data.csv"
    output_file = "processed_data.csv"

    etl_pipeline(input_file, output_file)


# =====================================================
# 7. ETL IN REAL MLOPS SYSTEM
# =====================================================
"""
Real-world MLOps ETL uses:
    - Apache Airflow (orchestration)
    - Apache Spark (big data processing)
    - Kafka (streaming)
    - Feature Store (training & inference consistency)
    - Data Validation tools (Great Expectations)

This script is the FOUNDATION
Advanced tools automate this logic
"""

# =====================================================
# 8. INTERVIEW QUESTIONS
# =====================================================
"""
Q1. Why ETL is important in MLOps?
    → Ensures clean, consistent & reproducible data

Q2. Difference between ETL & ELT?
    → ETL: Transform before load
    → ELT: Load first, transform later

Q3. What happens if ETL fails?
    → Model performance degrades

Q4. Which tool schedules ETL pipelines?
    → Apache Airflow
"""

# =====================================================
# END OF FILE
# =====================================================
