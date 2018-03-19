node ('master') {
    cleanWs()
    stage('checkout scm'){
        checkout scm
    }
    def pythonImage
    stage('build docker image'){
        pythonImage = docker.build('dec17win:test')
    }
    stage('test'){
        pythonImage.inside {
            bat '''. /tmp/venv/bin/activate && python - m pytest frame-test --junitxml=results.xml'''
        }
    }
    stage('collect test results'){
        junit 'results.xml'
    }
}