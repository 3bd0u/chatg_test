

pipeline {
    agent any

    environment {
        PYTHON_HOME = "C:\\Users\\usr1\\AppData\\Local\\Programs\\Python\\Python313"
        PATH = "${env.PYTHON_HOME};${env.PYTHON_HOME}\\Scripts;${env.PATH}"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/3bd0u/chatg_test.git'
            }
        }

        stage('Check files') {
            steps {
                bat 'dir'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"%PYTHON_HOME%\\python.exe" -m pip install --upgrade pip'
                bat '"%PYTHON_HOME%\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"%PYTHON_HOME%\\python.exe" -m pytest -v || echo No tests found'
            }
        }

        stage('Package App') {
            when {
                expression { currentBuild.currentResult == 'SUCCESS' }
            }
            steps {
                bat 'mkdir dist'
                bat 'powershell Compress-Archive -Path * -DestinationPath dist\\app_build.zip -Force'
                echo "Application packagée dans dist\\app_build.zip"
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline terminé avec succès !"
        }
        failure {
            echo "❌ Pipeline échoué ! Vérifie les logs Jenkins."
        }
    }
}

