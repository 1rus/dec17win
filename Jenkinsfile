node ('master') {
    cleanWs()
    stage('checkout scm'){
        checkout scm
    }
    def pythonImage
    stage('build docker image'){
        pythonImage = docker.build('dec17:test')
    }
    stage('test'){
        pythonImage.inside {
            sh '''. /tmp/venv/bin/activate && python3 - m pytest frame-test --junitxml=results.xml'''
        }
    }
    stage('collect test results'){
        junit 'results.xml'
    }
}