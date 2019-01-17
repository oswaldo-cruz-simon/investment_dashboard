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
        stage("Prepare external packages for container") {
            steps {
                script {
                    echo "Downloading Chrome Driver into workspace ..."
                    sh '''
                        wget https://chromedriver.storage.googleapis.com/2.40/chromedriver_linux64.zip
                        unzip chromedriver_linux64.zip
                        rm chromedriver_linux64.zip
                    '''
                    DRIVER_IN_WS = sh (
                        script: "ls | grep 'chromedriver'",
                        returnStdout: true
                    ).trim()
                    if ( DRIVER_IN_WS == "chromedriver") {
                        echo "Chrome Driver was downloaded into workspace."
                    } else{
                        echo("Chrome Driver was not downloaded into workspace. We could nor create docker image.")
                        currentBuild.result = 'ABORTED'
                    }
                }
            }
        }
        stage("Prepare external configuration for container") {
            environment {
                CONFIG_WORKSPACE = "/home/jfonseca/investment_dashboard/"
            }
            steps {
                script {
                    echo "Copy trusted into workspace ..."
                    sh '''
                        cp -f $CONFIG_WORKSPACE.credentials.yaml  ./.credentials.yaml
                    '''
                    CONFIG_IN_WS = sh (
                        script: "ls .credentials.yaml",
                        returnStdout: true
                    ).trim()
                    if ( CONFIG_IN_WS == ".credentials.yaml") {
                        echo "Configuration was copied into workspace."
                    } else{
                        echo("Configuration was not copied into workspace. We could not create docker image.")
                        currentBuild.result = 'ABORTED'
                    }
                }
            }
        }
        stage("Build Docker Image") {
            steps {
                script {
                    echo "Building scrapper Docker image ..."
                    def scrapperImage = docker.build("scraper:v1")
                    scrapperImage.inside {
                        sh '''
                         ls /app
                        '''
                    }
                }
            }
        }
        stage("Run scrapper") {
            steps {
                script {
                    echo "Running scrapper Docker image ..."
                    def scrapperImage = docker.image("scraper:v1")
                    scrapperImage.inside {
                        sh -c echo \"Hola \""
                    }
                    scrapperImage.run()

                }
            }
        }
    }
}