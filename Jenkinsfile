pipeline {
    agent any

    environment {
        IMAGE_NAME = "event-flow-app"
        IMAGE_TAG  = "${BUILD_NUMBER}"
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
                  docker build -t $IMAGE_NAME:$IMAGE_TAG .
                '''
            }
        }

        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv('sonar-server') {
                    sh '''
                      sonar-scanner \
                      -Dsonar.projectKey=event-flow-app \
                      -Dsonar.sources=.
                    '''
                }
            }
        }

        stage('Trivy Image Scan') {
            steps {
                sh '''
                  trivy image \
                  --severity HIGH,CRITICAL \
                  --exit-code 0 \
                  $IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }
    }

    post {
        success {
            echo "✅ CI Pipeline completed successfully"
        }
        failure {
            echo "❌ CI Pipeline failed"
        }
    }
}
