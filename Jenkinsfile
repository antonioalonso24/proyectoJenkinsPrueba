pipeline {
  agent any  // Usamos cualquier nodo que tenga Docker instalado

  stages {
    stage('Checkout') {
      steps {
        // Clona el repositorio con tu Jenkinsfile y el código
        checkout scm
      }
    }

    stage('Build & Test in Docker') {
      steps {
        // Ejecuta todo dentro de un contenedor Docker usando el binario Docker
        sh '''
          docker run --rm -u root:root \
            -v "$WORKSPACE":/workspace -w /workspace \
            python:3.10 bash -c "
              python -m venv venv && \
              . venv/bin/activate && \
              pip install --upgrade pip && \
              pip install -r requirements.txt && \
              pytest --verbose
            "
        '''
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
