CRON_SETTINGS = BRANCH_NAME == "main" ? '11 30 * * *' : ""
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
                echo "currentBuild.getBuildCauses()[0].shortDescription?:''"
                // Add build commands here
            }
        }
        stage('Check Cron') {
        steps {
            script {
                def buildCauses = currentBuild.getBuildCauses()
                // Log build causes in a more structured way
                buildCauses.each { cause ->
                    echo "Build Cause: ${cause.shortDescription}"
                }
                
                echo 'Building the application...'
                
                // More reliable way to detect timer-triggered builds
                if (currentBuild.getBuildCauses()[0].shortDescription?:''.contains('Started by timer')) {
                    triggered_by = 'Cron Job'
                    echo "Triggered by cron job"
                } else {
                    triggered_by = 'Manual or Other Trigger'
                    echo "Triggered by: ${triggered_by}"
                }
    }
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
