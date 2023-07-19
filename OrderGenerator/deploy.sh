aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 621130241729.dkr.ecr.us-east-1.amazonaws.com
docker build -t publish_order .
docker tag publish_order:latest 621130241729.dkr.ecr.us-east-1.amazonaws.com/publish_order:latest
docker push 621130241729.dkr.ecr.us-east-1.amazonaws.com/publish_order:latest
aws lambda update-function-code \
           --function-name PublishOrder \
           --image-uri 621130241729.dkr.ecr.us-east-1.amazonaws.com/publish_order:latest
docker image prune -a --force
docker system prune -a -y
read jainil