pipeline {
     agent {
        docker {
            image 'test_vnc:latest'
        }
     }
    stages {
        stage('Build Dependencies') {
            steps {
                    echo "###########  Install the requirements ########### "
                    sh 'pip install --upgrade pip'
                    echo "pip3 install -r ./requirements.txt"
                    sh 'pip install -r ./requirements.txt'
                    echo "Build Completed and requirement installed successfully"
            }
        }        
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh "python -m test1.py"
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }

}
