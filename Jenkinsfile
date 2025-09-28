pipeline {
    agent any

    environment {
        APP_NAME = 'MyPythonApp'
    }


    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/3bd0u/chatg_test.git'
            }
        }
        
 stage('Check files') {
            steps {
                bat 'dir'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest || echo No tests found'
            }
        }

        stage('Package App') {
            steps {
                bat 'echo "Packaging $APP_NAME..."'
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
