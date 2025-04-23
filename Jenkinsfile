pipeline {
  agent any  // Usamos cualquier nodo disponible

  stages {
    stage('Checkout') {
      steps {
        // Clona el repositorio con tu Jenkinsfile y el código
        checkout scm
      }
    }

    stage('Build & Test') {
      steps {
        // Intentamos con Docker; si no está disponible, usamos el entorno local
        sh '''
          echo "=== Build & Test Stage ==="
          if [ -x "$(command -v docker)" ]; then
            echo "Docker disponible: ejecutando en contenedor python:3.10"
            docker run --rm -u root:root \
              -v "$WORKSPACE":/workspace -w /workspace \
              python:3.10 bash -c "
                python -m venv venv && \
                . venv/bin/activate && \
                pip install --upgrade pip && \
                pip install -r requirements.txt && \
                pytest --verbose
              "
          else
            echo "Docker no encontrado: ejecutando localmente"
            python3 -m venv venv && \
            . venv/bin/activate && \
            pip install --upgrade pip && \
            pip install -r requirements.txt && \
            pytest --verbose
          fi
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
