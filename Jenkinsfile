node ('master') {
    cleanWs()
    stage('checkout scm'){
        checkout scm
    }
    def pythonImage
    stage('build docker image'){
	bat "docker build -t --name dec17win:test ."
 //       pythonImage = docker.build('dec17win:test')
    }
    stage('test'){
        
        bat "docker exec dec17win:test /tmp/venv/bin/activate && python - m pytest frame-test --junitxml=results.xml"
        
    }
    stage('collect test results'){
        bat "docker exec dec17win:test junit 'results.xml'"
    }
}