pipeline {
    environment {
        HOME_MSG="Hola"
    }
    stages {
        stage("Check hook") {
            steps {
                script{
                    sh '''
                      echo ${HOME_MSG}
                    '''
                }
            }
        }
    }
}