pipeline {
    agent any 
    stages {
        stage('Build') {
            steps {
                git 'https://github.com/cturra/docker-ntp.git'
                sh 'docker run --name=ntp            \
              --restart=always      \
              --detach              \
              --publish=123:123/udp \
              cturra/ntp'
              sh 'docker ps -a'
              sh 'docker exec ntp chronyc tracking'
            }
        }
    }
}
