pipeline {
    agent any
    environment {
        DOCKERFILE_NAME="DockerFile"
    }
    stages {
        stage("Check SCM files") {
            steps {
                script {
                    sh '''
                      echo "Checking SCM files"
                      DOCKER_FILE=$(ls . | grep ${DOCKERFILE_NAME} | grep -v grep)
                      echo $DOCKER_FILE
                      if [ -z "$DOCKER_FILE" ];
                      then
                        echo "Docker file is present on our checkout form SCM."
                      else
                        echo "Docker file is not present on our checkout form SCM. Aborting..."
                        exit 1
                      fi
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