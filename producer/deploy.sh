#!/bin/bash

echo "Starting deployment..."

# 1. Update and install core packages
sudo yum update -y
sudo yum install -y git python3 pip unzip
echo "Installed core packages..."


# 2. Clone your repo (skip if already present)
if [ ! -d "pipeline" ]; then
  git clone "repo"
fi

cd pipeline

# 3. Setup Python venv
python3 -m venv env
source env/bin/activate
echo "Python venv setup done..."


# 4. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
echo "Installed dependencies..."

# 5. AWS config setup
mkdir -p ~/.aws
cat <<EOL > ~/.aws/credentials
[default]
aws_access_key_id=YOUR_ACCESS_KEY
aws_secret_access_key=YOUR_SECRET_KEY
EOL

cat <<EOL > ~/.aws/config
[default]
region=ap-south-1
output=json
EOL

echo "AWS CLI setup done"

# OR set via env vars (safer for containers):
# export AWS_ACCESS_KEY_ID=...
# export AWS_SECRET_ACCESS_KEY=...
# export AWS_DEFAULT_REGION=ap-south-1

# 6. Run Uvicorn
echo "🚦 Starting Event Producer server..."
uvicorn producer.main:app --host 0.0.0.0 --port 8000
