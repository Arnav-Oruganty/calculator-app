pipeline {
    agent any

    environment {
        DOCKERHUB_REPO = "arnavoruganty/imt2023078-calculator"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-creds',
                    url: 'https://github.com/Arnav-Oruganty/calculator-app.git'
            }
        }

        stage('Install dependencies') {
            steps {
                sh "pip3 install -r requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                sh "pytest"
            }
        }

        stage('Build Docker Image') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                sh "docker build -t ${DOCKERHUB_REPO}:latest ."
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                                                 usernameVariable: 'USER',
                                                 passwordVariable: 'PASS')]) {
                    sh "echo $PASS | docker login -u $USER --password-stdin"
                    sh "docker push ${DOCKERHUB_REPO}:latest"
                }
            }
        }
    }
}
