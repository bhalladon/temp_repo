CRON_SETTINGS = BRANCH_NAME == "main" ? '10 23 * * *' : ""
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
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running tests...'
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
