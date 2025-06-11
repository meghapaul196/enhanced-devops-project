pipeline {
    agent any

    tools {
        maven 'Maven 3.9.6'
        jdk 'jdk21'
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

        stage('Build') {
            steps {
                bat 'mvn clean install'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    bat "${SONARQUBE_SCANNER_HOME}\\bin\\sonar-scanner.bat -Dsonar.projectKey=enhanced-devops-project -Dsonar.sources=. -Dsonar.java.binaries=target"
                }
            }
        }

        stage("Quality Gate") {
            steps {
                timeout(time: 1, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy step here (e.g., copy files, restart server, etc.)'
            }
        }
    }
}
