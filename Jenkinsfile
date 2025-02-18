CRON_SETTINGS = BRANCH_NAME == "main" ? '11 40 * * *' : ""
pipeline {
        docker {
            image 'sha256:e3713252a41cd3cd08ec84a13eb08e42b3768a15f122609e0f9f7548105f657c'
        }
    }
    stages {
        stage('Build Dependencies') {
            steps {
                    echo "###########  Install the requirements ########### "
                    sh 'pip3 install --upgrade pip'
                    echo "pip3 install -r ./requirements.txt"
                    sh 'pip3 install -r ./requirements.txt'
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
