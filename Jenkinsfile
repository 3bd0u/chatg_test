pipeline {
    agent any

    environment {
        APP_NAME = 'MyPythonApp'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/3bd0u/chatg_test.git'
                 credentialsId: '308b517e-cbbd-4cee-b1ba-d893ee674d4e'
            }
        }
        

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }

        stage('Package App') {
            steps {
                sh 'echo "Packaging $APP_NAME..."'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
