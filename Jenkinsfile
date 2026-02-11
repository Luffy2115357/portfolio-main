pipeline {
    agent any
    environment {
        // Professional Versioning: Uses Jenkins Build Number
        IMAGE_NAME = "luffy2115357/portfolio-app:${env.BUILD_NUMBER}"
        CONTAINER_NAME = "portfolio-container"
    }
    stages {
        stage('Build') {
            steps {
                echo "Building version ${env.BUILD_NUMBER}..."
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }
        stage('Test') {
            steps {
                echo "Running Unit Tests with Pytest..."
                // Ensures your Python code is valid before we dare to deploy it
                sh "docker run --rm ${IMAGE_NAME} python -m pytest"
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying version ${env.BUILD_NUMBER}..."
                // Remove the existing container so we can start the new version
                sh "docker rm -f ${CONTAINER_NAME} || true"
                sh "docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${IMAGE_NAME}"
            }
        }
    }
    post {
        success {
            echo "Successfully deployed Build #${env.BUILD_NUMBER}!"
        }
    }
}
