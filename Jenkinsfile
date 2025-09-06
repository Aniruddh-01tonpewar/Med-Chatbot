pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID     = credentials('aws-ec2-credentials')
        AWS_SECRET_ACCESS_KEY = credentials('aws-ec2-credentials')
        AWS_REGION            = "us-east-1"
        AWS_ACCOUNT_ID        = "077532334118"
        ECR_REPO_NAME         = "my-repo"
    }

    stages {
        stage('Checkout from GitHub') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Aniruddh-01tonpewar/Med-Chatbot.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                echo "Building Docker image..."
                docker build -t $ECR_REPO_NAME:latest .
                '''
            }
        }

        stage('Login to AWS ECR') {
            steps {
                sh '''
                echo "Logging in to Amazon ECR..."
                aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
                aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
                aws configure set default.region $AWS_REGION

                aws ecr get-login-password --region $AWS_REGION | \
                docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
                '''
            }
        }

        stage('Tag & Push to ECR') {
            steps {
                sh '''
                echo "Tagging image..."
                docker tag $ECR_REPO_NAME:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO_NAME:latest

                echo "Pushing image to ECR..."
                docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO_NAME:latest
                '''
            }
        }
    }
}
