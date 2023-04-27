FROM python:3.7-alpine AS backend-kubeflow-wheel

#WORKDIR /src
#COPY ./components/crud-web-apps/common/backend .

#RUN python3 setup.py bdist_wheel

#FROM python:3.7
#
#WORKDIR /package
#COPY --from=backend-kubeflow-wheel /src .
#RUN pip3 install .

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

RUN apk update && apk add --no-cache sudo bash openrc openssh
RUN echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config
RUN echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config
RUN mkdir -p /run/openrc && touch /run/openrc/softlevel && rc-update add sshd default
#RUN service sshd start -Z && service sshd start
#RUN echo "root:T3tDUcWNMQT5S" | chpasswd

CMD ["python", "/app/main.py"]
