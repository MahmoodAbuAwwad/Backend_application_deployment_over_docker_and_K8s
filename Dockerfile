FROM centos:centos7

RUN yum update
RUN yum install -y python
RUN yum install -y sqlite
RUN yum install -y git

RUN yum install -y epel-release
RUN yum install -y  python-pip
RUN pip install --upgrade pip
RUN pip install flask>=1.1.2

#personal token generated
RUN git clone https://6b9c241e78c2eab34b7f60a9896651abe1a8cf59@github.com/MahmoodAbuAwwad/backend_kubernetes.git

RUN pip install -r backend_kubernetes/requirements.txt
#ADD ./backend_kubernetes/main.py /opt/main.py

ENTRYPOINT FLASK_APP=backend_kubernetes/main.py flask run 
