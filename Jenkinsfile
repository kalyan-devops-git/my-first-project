pipeline {
    agent {
        label 'docker-agent'
    }
    environment {
        GCP_PROJECT = 'kalyan-devops-2025'
        IMAGE = "us-central1-docker.pkg.dev/kalyan-devops-2025/my-repo/my-first-project:v1"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh "docker build -t ${IMAGE} ."
            }
        }
        stage('Push') {
            steps {
                withCredentials([file(credentialsId: 'gcp-sa-key', variable: 'GCP_SA_KEY')]) {
                    sh """
                        gcloud auth activate-service-account --key-file=${GCP_SA_KEY}
                        gcloud config set project ${GCP_PROJECT}
                        gcloud auth configure-docker us-central1-docker.pkg.dev --quiet
                        docker push ${IMAGE}
                    """
                }
            }
        }
        stage('Deploy') {
            steps {
                sh "kubectl set image deployment/flask-app flask-app=${IMAGE} --record"
            }
        }
    }
}
