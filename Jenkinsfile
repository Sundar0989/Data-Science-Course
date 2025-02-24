pipeline {

    agent any

    stages {

        stage('Checkout') {

            steps {

                git branch: 'main', url: 'https://github.com/Sundar0989/Data-Science-Course.git'  

            }

        }

        stage('Build Docker Image') {

            steps {

                sh 'docker build -t sundar0989/demo_titanic_app .' 

            }

        }

        // stage('Run Docker Container') {

        //     steps {

        //         sh 'docker run -it demo_titanic_app bash' 

        //     }

        // }

    }

}