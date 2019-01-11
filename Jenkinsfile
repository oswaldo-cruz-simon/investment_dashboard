pipeline {
    agent any
    environment {
        HOME_MSG="Hola"
    }
    stages {
        stage("Check hook") {
            steps {
                script{
                    sh '''
                      echo "Connecting to remote server........."
                    '''
                }
            }
        }
    }
}