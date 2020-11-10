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


RUN mkdir ./app

RUN cp -r ./backend_kubernetes/* /app/.

WORKDIR ./app
RUN pip install -r requirements.txt
RUN pip install gunicorn
EXPOSE 5000

ENTRYPOINT ["gunicorn","--bind","0.0.0.0:5000", "main:app"]
