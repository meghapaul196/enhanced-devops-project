pipeline {
    agent any

    tools {
        jdk 'jdk21' // Required for SonarQube analysis
    }

    environment {
        SONARQUBE_SCANNER_HOME = tool 'SonarQube Scanner'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/meghapaul196/enhanced-devops-project.git'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    pytest --junitxml=pytest-report.xml --cov=. --cov-report=xml
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    withCredentials([string(credentialsId: 'sonarqube-token', variable: 'SONAR_TOKEN')]) {
                        bat """
                            ${SONARQUBE_SCANNER_HOME}\\bin\\sonar-scanner.bat ^
                            -Dsonar.projectKey=enhanced-devops-project ^
                            -Dsonar.sources=. ^
                            -Dsonar.language=py ^
                            -Dsonar.python.version=3.11 ^
                            -Dsonar.python.coverage.reportPaths=coverage.xml ^
                            -Dsonar.login=%SONAR_TOKEN%
                        """
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 60, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('Deploy') {
            steps {
                echo '🚀 Deployment steps go here (e.g., upload to server, Docker deploy, etc.)'
            }
        }
    }
}
