CRON_SETTINGS = BRANCH_NAME == "main" ? '10 55 * * *' : ""
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
                if (env.BUILD_DESCRIPTION.contains("Started by timer")) {
                    triggered_by = "Cron Job"
                    echo "Triggered by cron job"
                }
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
