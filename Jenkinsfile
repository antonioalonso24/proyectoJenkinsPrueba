pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        // Crear el entorno virtual
        sh 'python3 -m venv venv'
        // Activar el entorno virtual
        sh '. venv/bin/activate'
        // Asegurarnos de que pip esté disponible y actualizado
        sh 'python3 -m pip install --upgrade pip'
        // Instalar dependencias
        sh 'python3 -m pip install -r requirements.txt'
      }
    }
    stage('Test') {
      steps {
        // Activar el entorno virtual antes de ejecutar tests
        sh '. venv/bin/activate'
        // Ejecutar pytest
        sh 'python3 -m pytest --maxfail=1 --disable-warnings -q'
      }
    }
    stage('Deploy') {
      steps {
        // Simulación de despliegue
        sh 'echo "Despliegue simulado"'
      }
    }
  }
}
