# backend_kubernetes


- build the Docker Image

  docker build -t mahmoodabuawwad/backend . --no-cache

- run mysql container 
  
  
  docker run --name mysql -t --net=host -e MYSQL_DATABASE="backend" -e MYSQL_USER="flask" -e MYSQL_PASSWORD="flask" -e MYSQL_ROOT_PASSWORD="flask" -d mysql

- run new container


  docker run --name mysql -t --net=host -e MYSQL_DATABASE="backend" -e MYSQL_USER="flask" -e MYSQL_PASSWORD="flask" -e MYSQL_ROOT_PASSWORD="flask" -d mysql


- run backend container


  docker run -d --name backend --net=host -e "PORT=3306" -e "HOST=192.168.204.226" mahmoodabuawwad/backend


* if errors occured, u may need to execute the follwing to get the right permissions in mysql container
  - docker exec -it mysql mysql -p -u root 
  - grant all privileges on backend.* to 'flask';
  - grant all privileges on backend.* to 'root';

- create Deployments and services using flask-dep.yam/flask-ser.yaml/mysql-dep.yam/mysql-ser.yaml






