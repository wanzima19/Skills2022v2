pipeline {
    agent any

    stages {
       stage('build') {
            steps {
                sh 'docker run -e CI=true -v $JENKINS_INSTALL$PWD:/usr/src/app zenika/alpine-node yarn build'
            }
        }
        stage('deploy') {
            steps {
                sh 'docker build -t local/application:${BRANCH_NAME} $PWD'
                sh 'docker-compose -p ${BRANCH_NAME}-demo up -d'
            }
        }
    }
}
