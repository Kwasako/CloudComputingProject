# CloudComputingProject
# Task
The task is to create a lambda function that connects and processes the financial data flat file for JPMorgan Chase company. The file has 7 original columns for; Date, Open, High, Low, Close, Adj Close, and Volume. 
the function should add two new columns to the table.
I. Daily range - Which is the difference between the open and close columns for every row.
Ii. Daily span - The difference between the high and low values for every row.
# Solutions
AWS lambda, AWS IAM, AWS S3, AWS Lambda was used for this project, 
AWS Lambda was used to create a Lambda function for the implementation of the data pipeline
AWS IAM was used to create a role that provide access to AWS S3 bucket and AWS Event Bridge, 
finally AWS S3 was used to create a bucket inside which the source & destination folders were created.  
note: the JPMorgan Chase company stock data was uploaded to the source folder in the S3 budket 
The Lambda function was configured to use additional code and content in the form of layers.
The layers was extracted using AWS ARN for Lambda and the ARN that corresponds with region and python version was obtain from - https://aws-sdk-pandas.readthedocs.io/en/stable/layers.html
