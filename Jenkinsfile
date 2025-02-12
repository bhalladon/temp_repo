CRON_SETTINGS = BRANCH_NAME == "main" ? '10 59 * * *' : ""
pipeline {
    agent any
    triggers {
        cron(CRON_SETTINGS)
    }
    stages {
        stage('Build') {
            steps {
                script {
                    if (${currentBuild.getBuildCauses()[0].shortDescription?:''}.contains("Started by timer")) {
                    triggered_by = "Cron Job"
                    echo "Triggered by cron job"
                }
                }
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
