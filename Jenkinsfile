pipeline {
    agent any

    environment {
        PYTHON_PATH = "C:\\Users\\USER\\AppData\\Local\\Python\\bin\\python.exe"
        DEPLOY_SERVER = "aws-prod"
        DEPLOY_PATH = "/home/ubuntu/chatg_test"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/3bd0u/chatg_test.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat "${env.PYTHON_PATH} -m pip install --upgrade pip"
                bat "${env.PYTHON_PATH} -m pip install -r requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                bat "${env.PYTHON_PATH} -m pytest --maxfail=1 --disable-warnings -q"
            }
        }

        stage('Package App') {
            steps {
                bat 'powershell Compress-Archive -Path * -DestinationPath app_build.zip -Force'
            }
        }

        stage('Deploy to AWS') {
            steps {
                echo '🚀 Déploiement sur le serveur AWS EC2...'
                sshPublisher(publishers: [
                    sshPublisherDesc(
                        configName: "${env.DEPLOY_SERVER}",
                        transfers: [
                            sshTransfer(
                                sourceFiles: 'app_build.zip',
                                removePrefix: '',
                                remoteDirectory: "${env.DEPLOY_PATH}",
                                execCommand: '''
                                    cd ${DEPLOY_PATH}
                                    unzip -o app_build.zip
                                    echo "✅ Déploiement terminé sur AWS"
                                '''
                            )
                        ]
                    )
                ])
            }
        }
    }

    post {
        success {
            echo '🎉 Pipeline réussi et application déployée sur AWS !'
        }
        failure {
            echo '❌ Pipeline échoué. Vérifie les logs Jenkins.'
        }
    }
}
