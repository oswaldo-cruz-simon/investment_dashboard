pipeline {
    agent any
    environment {
        HOME_MSG="Hola"
    }
    stages {
        stage("Check SCM files") {
            steps {
                script {
                    sh '''
                      echo "Checking SCM files"
                      ls .
                      DOCKER_FILE=$(ls. | grep DockerFile | grep -v grep)
                      echo $DOCKER_FILE
                    '''
                }
            }
        }
        stage("Build Docker Image") {
            steps {
                script {
                    sh '''
                        echo "Here we run: docker build -t scraper:v1 if all files needed"
                    '''
                }
            }
        }
    }
}