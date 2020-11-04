FROM centos:centos7

RUN yum update
RUN yum install -y python
RUN yum install -y sqlite
Run yum install -y git

RUN yum install -y epel-release
RUN yum install -y  python-pip
RUN pip install flask>=1.1.2
RUN git clone git@github.com:MahmoodAbuAwwad/backend_kubernetes.git
RUN pip install -r backend_kubernetes/requirements.txt
COPY backend_kubernetes/main.py /opt/main.py

ENTRYPOINT FLASK_APP=/opt/main.py flask run

