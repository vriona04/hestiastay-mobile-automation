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
                adb shell am force-stop com.hostelrs.guest
                timeout /t 5

                adb shell monkey -p com.hostelrs.guest -c android.intent.category.LAUNCHER 1
                timeout /t 10
                '''
            }
        }

        stage('Run Automation Tests') {
            steps {
                bat '''
                if not exist reports mkdir reports
                if not exist screenshots mkdir screenshots

                "C:\\Program Files\\Python312\\python.exe" -m pytest -v -s ^
                tests/test_auto_login_fixture.py ^
                tests/test_booking_details.py ^
                tests/test_food_menu.py ^
                tests/test_support_tickets.py ^
                --html=reports/jenkins_report.html --self-contained-html
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
            reportFiles: 'jenkins_report.html',
            reportName: 'HestiaStay Automation Report'
        ])

        archiveArtifacts artifacts: 'screenshots/**/*', fingerprint: true
    }
}