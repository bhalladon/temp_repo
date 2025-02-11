CRON_SETTINGS = BRANCH_NAME == "main" ? '5 23 * * *' : ""
pipeline {
    agent any
    triggers {
        cron(CRON_SETTINGS)
    }
    stages {
        stage('Build') {
            steps {
                echo "${currentBuild.getBuildCauses()}"
                echo 'Building the application...'
                // Add build commands here
                sh 'mvn clean compile'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'mvn test'
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
