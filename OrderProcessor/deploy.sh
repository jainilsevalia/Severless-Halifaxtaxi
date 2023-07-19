aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 621130241729.dkr.ecr.us-east-1.amazonaws.com
docker build -t poll_msg_send_mail .
docker tag poll_msg_send_mail:latest 621130241729.dkr.ecr.us-east-1.amazonaws.com/poll_msg_send_mail:latest
docker push 621130241729.dkr.ecr.us-east-1.amazonaws.com/poll_msg_send_mail:latest
aws lambda update-function-code \
           --function-name poll_msg_send_mail_function\
           --image-uri 621130241729.dkr.ecr.us-east-1.amazonaws.com/poll_msg_send_mail:latest
docker image prune -a --force
docker system prune -a -y
read jainil