pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        // Clona el repositorio con tu Jenkinsfile y el código
        checkout scm
      }
    }

    stage('Build & Test in Docker') {
      steps {
        script {
          // Usa la imagen oficial de Python 3.10
          docker.image('python:3.10').inside('-u root:root') {
            sh '''
              python -m venv venv               # crea el virtualenv
              . venv/bin/activate              # activa
              pip install --upgrade pip        # actualiza pip
              pip install -r requirements.txt  # instala dependencias
              pytest --verbose                 # lanza tus tests
            '''
          }
        }
      }
    }

    stage('Deploy') {
      steps {
        // Simulación de despliegue
        echo 'Despliegue simulado exitoso'
      }
    }
  }
}
