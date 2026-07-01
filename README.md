# Healthcare AWS Data Engineering Project

## Overview

This project demonstrates an end-to-end healthcare data engineering
pipeline on AWS. Raw healthcare CSV datasets are ingested into Amazon
S3, transformed into optimized Parquet format using AWS Glue (PySpark),
cataloged in AWS Glue Data Catalog, and queried using Amazon Athena.

> **Current Status:** Completed through the curated analytics layer.
> Incremental loading is planned as the next enhancement.

------------------------------------------------------------------------

## Architecture

``` text
Healthcare CSV Files
        │
        ▼
Amazon S3 (Landing)
        │
        ▼
AWS Glue ETL (PySpark)
        │
        ▼
Amazon S3 (Curated - Parquet)
        │
        ▼
AWS Glue Data Catalog
        │
        ▼
Amazon Athena
        │
        ▼
SQL Analytics
```

------------------------------------------------------------------------

## AWS Services Used

-   Amazon S3
-   AWS Glue 5.1
-   PySpark
-   AWS Glue Data Catalog
-   Amazon Athena
-   IAM
-   CloudWatch Logs

------------------------------------------------------------------------

## Dataset

The project processes the following healthcare datasets:

-   patient
-   provider
-   hospital
-   coverage
-   preauth_case
-   preauth_los
-   preauth_review
-   authorization_days
-   case_flags
-   peer_review
-   notifications
-   member_letters

------------------------------------------------------------------------

## ETL Workflow

### Landing Layer

Raw CSV files are stored in:

    s3://<bucket>/landing/

### Curated Layer

Glue converts CSV files into Parquet format and stores them in:

    s3://<bucket>/curated/

------------------------------------------------------------------------

## Glue ETL Features

-   Generic ETL job for multiple datasets
-   Dynamic processing using a table list
-   CSV to Parquet conversion
-   Infer schema
-   Logging for every table
-   Exception handling using try/except
-   Processing summary
-   Row count validation
-   Empty file validation
-   NULL value validation
-   Duplicate record validation
-   Patient-specific validations:
    -   Gender validation
    -   Date of Birth validation

------------------------------------------------------------------------

## Athena

All curated datasets are available through Athena.

Example analyses completed:

-   Total patients
-   Patients by state
-   Patients by gender
-   Top groups
-   Coverage analysis
-   Hospital case analysis
-   Provider approval analysis
-   Multi-table joins
-   Window functions
-   Ranking
-   CTE-based reporting

------------------------------------------------------------------------

## Skills Demonstrated

-   AWS Glue
-   PySpark
-   Amazon Athena
-   SQL
-   Data Validation
-   ETL Design
-   Cloud Data Engineering
-   Data Quality Checks
-   Parquet Optimization
-   Logging and Monitoring

------------------------------------------------------------------------

## Current Project Status

Completed: - Landing layer - Curated layer - Glue ETL - Data
validation - Athena integration - Business SQL analysis

Planned: - Incremental loading - Glue Job Bookmarks / Merge strategy -
Glue Workflows - Power BI Dashboard - GitHub CI documentation

------------------------------------------------------------------------

## Repository Structure

``` text
healthcare-aws-project/
│
├── glue/
├── sql/
├── architecture/
├── screenshots/
├── README.md
```
