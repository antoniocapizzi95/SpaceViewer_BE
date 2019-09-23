pipeline {
    agent {
        docker {
            image 'jfloff/alpine-python'
            args '-p 5001:5001 --name backend'
            }
        }
        stages {

            stage('Install Dependencies') {
                         steps {
                             //sh 'pip install --upgrade pip'
                             sh 'pip install flask'
                             sh 'pip install requests'
                             sh 'pip install -U flask-cors'
                             sh 'pip install gunicorn'
                         }
                     }

             stage('Deliver') {
                         steps {
                             sh 'gunicorn -b 0.0.0.0:5001 api:app &'
                             input message: 'Click "proceed" to stop the job'
                         }
                     }
        }
}