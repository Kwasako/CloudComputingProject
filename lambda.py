import json
import boto3
import csv
import pandas as pd
import tempfile
import datetime

def lambda_handler(event, context):
    # Get the source bucket and key from the event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_key = event['Records'][0]['s3']['object']['key']

    # Create an S3 client
    s3 = boto3.client('s3')

    # Download the CSV file from S3
    response = s3.get_object(Bucket=source_bucket, Key=source_key)
    csv_data = response['Body'].read().decode('utf-8')

    # Create a temporary file to store the CSV data
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
    temp_file.write(csv_data)
    temp_file.close()

    # Create a DataFrame from the CSV data
    df = pd.read_csv(temp_file.name)

    df['daily range'] = df['Open'] - df['Close']
    df['daily span'] = df['High'] - df['Low']
    
    # Convert the DataFrame back to CSV data
    csv_data_processed = df.to_csv(index=False)

    # Upload the processed data to a separate location
    time = datetime.datetime.now()
    target_bucket = '10alyticstest-bucket'
    target_key = f'processed/{time}.csv'
    
    
    s3.put_object(Body=csv_data_processed, Bucket=target_bucket, Key=target_key)

    return {
        'statusCode': 200,
        'body': 'CSV processing completed successfully.'
    }
