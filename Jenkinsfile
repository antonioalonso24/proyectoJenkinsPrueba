pipeline {
  // Usamos Docker: cada etapa correrá dentro de un contenedor python:3.10
  agent {
    docker {
      image 'python:3.10'    // imagen oficial que trae python3-venv y pip
      args  '-u root:root'   // opcional: ejecutar como root (por ejemplo, si necesitas instalar deps de SO)
    }
  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm         // baja tu repositorio (incluye el Jenkinsfile)
      }
    }
    stage('Build') {
      steps {
        // Agrupamos en un solo shell para que el entorno virtual persista en este contenedor
        sh '''
          python -m venv venv               # crea el virtualenv
          . venv/bin/activate              # activa
          pip install --upgrade pip        # actualiza pip
          pip install -r requirements.txt  # instala tus dependencias
        '''
      }
    }
    stage('Test') {
      steps {
        sh '''
          . venv/bin/activate      # vuelves a activar el venv
          pytest --verbose         # lanzas tus tests
        '''
      }
    }
    stage('Deploy') {
      steps {
        // Simulación de despliegue
        sh 'echo "Despliegue simulado exitoso"'
      }
    }
  }
}
