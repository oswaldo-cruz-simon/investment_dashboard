pipeline {
    agent any
    environment {
        DOCKERFILE_NAME="Dockerfile"
    }
    stages {
        stage("Check SCM files") {
            steps {
                script {
                    sh '''
                      echo "Checking SCM files in workspace ..."
                      DOCKER_FILE=$(ls . | grep ${DOCKERFILE_NAME} | grep -v grep)
                      echo $DOCKER_FILE
                      if [ -n "$DOCKER_FILE" ];
                      then
                        echo "Docker file is present on our workspace from SCM checkout."
                      else
                        echo "Docker file is present on our workspace from SCM checkout. Aborting."
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
                        echo "Building scrapper Docker image ..."
                        docker build -t scraper:v1 .
                    '''
                }
            }
        }
    }
}