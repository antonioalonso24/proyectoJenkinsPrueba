pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'source venv/bin/activate && python3 -m pytest --verbose'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Despliegue simulado exitoso"'
            }
        }
    }
}
