pipeline {
  agent {
    docker {
      image 'python:3.10'
      args '-u root:root -v $PWD:$PWD -w $PWD'
    }
  }
  stages {
    stage('Build') {
      steps {
        // Crear y activar entorno virtual
        sh 'python3 -m venv venv'
        sh '. venv/bin/activate'
        // Actualizar pip e instalar dependencias
        sh 'python3 -m pip install --upgrade pip'
        sh 'python3 -m pip install -r requirements.txt'
      }
    }
    stage('Test') {
      steps {
        sh '. venv/bin/activate'
        sh 'python3 -m pytest --maxfail=1 --disable-warnings -q'
      }
    }
    stage('Deploy') {
      steps {
        sh 'echo "Despliegue simulado"'
      }
    }
  }
}
