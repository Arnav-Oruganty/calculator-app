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
                sh "python3 -m pytest"
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKERHUB_REPO}:latest ."
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                                                 usernameVariable: 'DOCKER_USER',
                                                 passwordVariable: 'DOCKER_PASS')]) {
        
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push arnavoruganty/imt2023078-calculator:latest
                    '''
                }
            }
        }
    }
}
