# 🧠 Lambda Image Analyzer

An event-driven AWS Lambda function that automatically analyzes images uploaded to an S3 bucket using Amazon Rekognition. Designed for real-time label detection and logging via CloudWatch, this project demonstrates serverless architecture, AI integration, and secure cloud-native design.

---

## 🚀 Architecture Overview

- **S3 Bucket** (`tammy-image-analyzer`): Stores uploaded `.jpg` or `.png` images
- **Lambda Function** (`ImageRekognitionHandler`): Triggered on image upload, invokes Rekognition
- **Amazon Rekognition**: Detects labels and confidence scores from the image
- **CloudWatch Logs**: Captures analysis results for review and debugging

---

## 🛠️ Technologies Used

- AWS Lambda (Python 3.13)
- Amazon S3
- Amazon Rekognition
- AWS CloudWatch
- IAM Roles and Policies
- Region: `eu-west-2` (London)

---

## 📦 File Structure

## 🧪 How It Works

1. Upload an image to the S3 bucket (e.g., `uploads/player1.jpg`)
2. S3 triggers the Lambda function
3. Lambda calls Rekognition to detect labels
4. Results are printed to CloudWatch Logs

## 🔐 IAM Role Requirements

Attach the following policies to your Lambda execution role:
- `AmazonRekognitionFullAccess`
- `AmazonS3ReadOnlyAccess`
- `CloudWatchLogsFullAccess`

## 📈 Sample Output (CloudWatch)

## 🧩 Future Enhancements

- Store results in DynamoDB for querying
- Trigger SNS alerts for specific labels
- Add pre-signed URL upload support
- Automate deployment with CloudFormation or Terraform

## 🧑‍💻 Author

**Tammy**
Cloud-native builder | AWS Solutions Architect in training | Passionate about playful, secure tech for young footballers

## 📄 License

MIT License – feel free to fork, adapt, and build on it!
