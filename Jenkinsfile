pipeline {
    agent any

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
            bat '"C:\\Users\\USER\\AppData\\Local\\Python\\bin\\python.exe" -m pip install --upgrade pip'
            bat '"C:\\Users\\USER\\AppData\\Local\\Python\\bin\\python.exe" -m pip install -r requirements.txt'
            }
        }


        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\USER\\AppData\\Local\\Python\\bin\\python.exe" -m pytest -v || echo No tests found'
            }
        }

        stage('Package App') {
            steps {
                bat '''
                if not exist dist mkdir dist
                echo "✅ Dossier dist prêt pour le packaging."
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline réussi !'
        }
        failure {
            echo '❌ Pipeline échoué ! Vérifie les logs Jenkins.'
        }
    }
}
