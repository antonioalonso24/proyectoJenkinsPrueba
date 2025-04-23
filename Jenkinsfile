pipeline {
  agent any

  stages {
    stage('Build') {
      steps {
        // Crear y activar el entorno virtual, luego instalar las dependencias
        sh '''
          python3 -m venv venv
          . venv/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
        '''
      }
    }
    stage('Test') {
      steps {
        // Ejecutar pruebas con pytest
        sh '. venv/bin/activate && python3 -m pytest'
      }
    }
    stage('Deploy') {
      steps {
        // Despliegue simulado
        sh 'echo "Despliegue simulado"'
      }
    }
  }
}
