pipeline {
agent any
stages {
	stage('Build') {
	parallel {
		stage('Build') {
		steps {
			sh 'Building Done"'
		}
		}
	}
	}

	stage('Test') {
	steps {
		sh 'Test building done'
	}
	}

	stage('Deploy')
	{
	steps {
		sh 'Deploy done'
	}
	}
}

post {
		always {
			echo 'The pipeline completed'
      emailext body: 'summary' subject: 'Pipeline status ' to: 'heroorkrishna@gmail.com' 
		}
		success {				
			echo "Flask Application Up and running!!"
		}
		failure {
			echo 'Build stage failed'
			error('Stopping early…')
		}
	}
}
