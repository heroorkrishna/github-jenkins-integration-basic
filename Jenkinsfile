pipeline {
   agent any
   stages {
      stage('Build') {
	  steps {
	     sh 'Building Done"'
	  }
      }
      stage('Deploy'){
	 steps {
	    sh 'Deploy done'
	 }
      }
      stage('Test') {
	  steps {
	    sh 'Test building done'
          }
      }
   }
   post {
	always {
	    echo 'The pipeline completed'
     	    emailext body: 'summary' subject: 'Pipeline status ' to: 'heroorkrishna@gmail.com' 
	}
}
