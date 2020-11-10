pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Tests'){
            steps {
                sh 'python main.py'
                junit 'reports/**/*.xml'
            }
            post {
                always {
                    junit 'reports/**/*.xml'

                }
            }
        }
    }