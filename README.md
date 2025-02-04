# AWS Image Classification 🚀

This project uses **AWS Rekognition** to classify objects in images uploaded to **Amazon S3**.

## Features
- Upload images to an S3 bucket.
- Perform image classification using AWS Rekognition.
- Retrieve detected labels with confidence scores.

## Installation
```bash
# Clone the repository
git clone https://github.com/sivaa-s/aws-image-classification.git
cd aws-image-classification

# Install dependencies
pip install boto3
```

## Setup
1. **AWS Credentials:** Ensure you have AWS credentials configured.
   ```bash
   aws configure
   ```
2. **Create an S3 bucket** and update `S3_BUCKET` in the script.
3. **Set up IAM permissions** to allow access to Rekognition and S3.

## Usage
```python
python classify.py --image path/to/your/image.jpg
```

## Project Structure
```
aws-image-classification/
│── src/               # Source code
│   ├── classify.py    # Image classification script
│   ├── s3_helper.py   # S3 upload helper functions
│── examples/          # Sample images
│── README.md          # Project documentation
│── requirements.txt   # Python dependencies
```

## Example Output
```json
[
    {"Label": "Dog", "Confidence": 98.5},
    {"Label": "Animal", "Confidence": 99.0}
]
```

## Contributing
Feel free to fork and contribute! Pull requests are welcome.

## License
MIT License.
