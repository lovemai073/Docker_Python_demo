# Docker_Python_demo
$ docker build -t docker-python-demo .    
  
$ docker images.   
REPOSITORY                                                                 TAG                 IMAGE ID            CREATED.   
docker-python-demo                                                         latest              7bfdbd393941        6 seconds ago        943MB
    
$ docker run -d -p 8080:80 docker-python-demo.     

$ curl -i http://localhost:8080.     

$ docker logs 3af20e876a01.   
