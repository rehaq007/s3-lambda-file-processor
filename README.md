#Automating S3 File Processing with AWS Lambda

Overview

This guide walks you through setting up an AWS Lambda function that automatically processes files uploaded to an S3 bucket. The function will:

✅ Trigger when a file is uploaded to the inbound/ folder in an S3 bucket.
✅ Transform the file content (convert text to uppercase).
✅ Move the transformed file to the archive/ folder.
✅ Delete the original file from inbound/.
✅ Delete the archived file automatically after 1 day.

This setup is perfect for automating data pipelines, cleaning data before analysis, or organizing file storage efficiently.

Prerequisites

Before you begin, make sure you have:

An AWS account

IAM permissions to create Lambda functions, S3 buckets, and CloudWatch logs

Basic understanding of AWS S3 and Lambda (no worries if you're a complete beginner, just follow the steps!)

Step-by-Step Implementation

Step 1: Create an S3 Bucket

If you already have an S3 bucket, you can skip this step. Otherwise:

Go to the AWS S3 Console.

Click Create bucket.

Enter a unique Bucket name (e.g., your-bucket-name).

Choose a region close to your users.

Click Create bucket.

Inside the bucket, create two folders:

inbound/ → Files will be uploaded here.

archive/ → Transformed files will be moved here.

Step 2: Create an IAM Role for Lambda

Lambda needs permission to read from and write to S3. To set up the permissions:

Go to AWS IAM Console → Roles.

Click Create role.

Choose AWS service → Lambda.

Click Next → Attach the AmazonS3FullAccess policy.

Click Next, name the role LambdaS3AccessRole, and click Create role.

Also, attach the AWSLambdaBasicExecutionRole policy to the same role. This allows Lambda to write logs to CloudWatch.

Step 3: Create the AWS Lambda Function

Go to the AWS Lambda Console.

Click Create function → Author from scratch.

Enter the function name: S3FileProcessor.

Select Python 3.9 as the runtime.

Under Permissions, choose Use an existing role and select LambdaS3AccessRole.

Click Create function.

Step 4: Upload the Python Script

Scroll down to the Code source section.

Upload your Python script (you'll place it in your GitHub repository under code/).

Click Deploy.

Step 5: Configure S3 to Trigger the Lambda Function

Go to the AWS S3 Console.

Open your S3 bucket.

Click the Properties tab.

Scroll down to Event notifications → Click Create event notification.

Enter a name: S3FileUploadTrigger.

Event Type: Select PUT (this triggers the function when a file is uploaded).

Prefix: Enter inbound/ (so only files in inbound/ trigger Lambda).

Destination: Choose Lambda function → Select S3FileProcessor.

Click Save.

Step 6: Set Up Automatic Deletion After 1 Day

Go to AWS S3 Console.

Open your S3 bucket.

Click the Management tab.

Click Create lifecycle rule.

Rule name: DeleteArchivedFiles.

Scope: Select Prefix and enter archive/.

Under Lifecycle rule actions, choose Expire current versions of objects.

Set the Number of days after object creation to 1.

Click Create rule.

Step 7: Testing the Setup

Upload a text file (e.g., test.txt) into inbound/ in your S3 bucket.

Check the Lambda function logs in CloudWatch.

The file should be:

Transformed (converted to uppercase).

Moved to the archive/ folder.

Deleted from inbound/.

After 1 day, the file in archive/ should be automatically deleted.

Real-World Use Cases

✅ Automating ETL pipelines – Pre-process files before loading into databases.✅ Data transformation – Convert data formats, clean text files, enrich metadata.✅ Log processing – Store logs in S3, trigger Lambda to process them.✅ File organization – Move files between folders for better structuring.

Conclusion

With this simple setup, we automated S3 file handling using AWS Lambda. This is a powerful pattern for serverless data processing and is widely used in real-world applications!

If you found this useful, feel free to contribute or suggest improvements! 🚀

#AWS #Lambda #S3 #Automation #DataEngineering

