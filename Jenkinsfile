pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        // 1) Crear el virtualenv
        sh 'python3 -m venv venv'
        // 2) Instalar deps vía python -m pip
        sh '. venv/bin/activate && python3 -m pip install -r requirements.txt'
      }
    }
    stage('Test') {
      steps {
        // Activar y lanzar pytest
        sh '. venv/bin/activate && python3 -m pytest --maxfail=1 --disable-warnings -q'
      }
    }
    stage('Deploy') {
      steps {
        sh 'echo "Despliegue simulado"'
      }
    }
  }
}
