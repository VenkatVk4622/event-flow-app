pipeline {
    agent any

    environment {
        AWS_REGION = "us-east-1"
        ECR_REPO   = "event-flow-app"
        IMAGE_TAG  = "${BUILD_NUMBER}"
        ACCOUNT_ID = "509399632114"   // your AWS account ID
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                  docker build -t $ECR_REPO:$IMAGE_TAG .
                '''
            }
        }

        stage('ECR Login') {
            steps {
                sh '''
                  aws ecr get-login-password --region $AWS_REGION \
                  | docker login --username AWS \
                    --password-stdin $ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
                '''
            }
        }

        stage('Docker Tag') {
            steps {
                sh '''
                  docker tag $ECR_REPO:$IMAGE_TAG \
                  $ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO:$IMAGE_TAG
                '''
            }
        }

        stage('Docker Push') {
            steps {
                sh '''
                  docker push $ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO:$IMAGE_TAG
                '''
            }
        }
    }

    post {
        success {
            echo " Docker image pushed to ECR (us-east-1) successfully"
        }
        failure {
            echo " CI Pipeline failed"
        }
    }
}
