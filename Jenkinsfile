pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                git 'https://github.com/alpinelinux/docker-alpine.git'
                sh 'docker run -it --rm alpine'
                     
                sh 'docker ps -a'
             
                     }
                  }
    }
}
