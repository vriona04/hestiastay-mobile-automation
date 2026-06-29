pipeline {
    agent any

    options {
        disableConcurrentBuilds()
    }

    environment {
        PYTHONPATH = 'C:\\Users\\ajayk\\AppData\\Roaming\\Python\\Python312\\site-packages'
    }

    stages {

        stage('Prepare Device') {
            steps {
                bat '''
                "C:\\Users\\ajayk\\AppData\\Local\\Android\\Sdk\\platform-tools\\adb.exe" shell am force-stop com.hostelrs.guest

                ping 127.0.0.1 -n 6 > nul

                "C:\\Users\\ajayk\\AppData\\Local\\Android\\Sdk\\platform-tools\\adb.exe" shell monkey -p com.hostelrs.guest -c android.intent.category.LAUNCHER 1

                ping 127.0.0.1 -n 11 > nul
                '''
            }
        }

        stage('Run Full Regression Suite') {
            steps {
                bat '''
                call run_regression.bat
                '''
            }
        }
    }

    post {

        always {

            publishHTML([
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'final_regression.html',
                reportName: 'HestiaStay Automation Report'
            ])

            archiveArtifacts(
                artifacts: 'screenshots/**/*',
                fingerprint: true,
                allowEmptyArchive: true
            )
        }

        success {
            echo 'Regression Suite Passed Successfully'
        }

        failure {
            echo 'Regression Suite Failed'
        }
    }
}