pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building the Docker Image...'
                sh 'docker build -t my-portfolio-app .'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying to Port 5000...'
                sh 'docker rm -f portfolio-container || true'
                sh 'docker run -d --name portfolio-container -p 5000:5000 my-portfolio-app'
                // Give the app 5 seconds to "wake up"
                sh 'sleep 5'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing: Is the website actually running?'
                // This checks if the website returns the success code "200"
                sh 'curl -s -o /dev/null -w "%{http_code}" http://localhost:5000 | grep 200'
            }
        }
    }
    post {
        success {
            echo 'Everything works! Your site is live.'
        }
        failure {
            echo 'Something went wrong. The app is broken!'
        }
    }
}
