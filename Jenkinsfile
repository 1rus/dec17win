node ('master') {
    cleanWs()
    stage('checkout scm'){
        checkout scm
    }
    def pythonImage
    stage('build docker image'){
	bat "docker build -t dec17win:test . && \
		docker run -d -it --name dec17win dec17win:test bash"
 //       pythonImage = docker.build('dec17win:test')
    }
    stage('test'){
        
        bat "docker exec -u root -it dec17win /tmp/venv/bin/activate && python - m pytest frame-test --junitxml=results.xml"
        
    }
    stage('collect test results'){
        bat "docker exec dec17win:test junit 'results.xml'"
    }
}