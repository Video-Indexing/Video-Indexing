#!/bin/bash
sudo yum install jq -y
sudo yum install git -y
echo -e "Host github.com\n\tStrictHostKeyChecking no" > ~/.ssh/config
chmod 600 ~/.ssh/config
sudo aws ssm get-parameter --region us-west-2 --name id_rsa.pub --with-decryption --query Parameter.Value --output text > ~/.ssh/id_rsa.pub && sudo chmod 400 ~/.ssh/id_rsa.pub
sudo aws ssm get-parameter --region us-west-2 --name id_rsa --with-decryption --query Parameter.Value --output text > ~/.ssh/id_rsa && sudo chmod 400 ~/.ssh/id_rsa
git clone git@github.com:Video-Indexing/Video-Indexing.git
sudo yum install docker -y
sudo systemctl enable docker.service
sudo systemctl start docker.service
cd Video-Indexing
cd Node_Web_Server
sudo aws ssm get-parameter --region us-west-2 --name serviceAccount --with-decryption --query Parameter.Value --output text > ~/Video-Indexing/Node_Web_Server/serviceAccount.json
sudo aws ssm get-parameter --region us-west-2 --name .env --with-decryption --query Parameter.Value --output text > ~/Video-Indexing/Node_Web_Server/.env
chmod +x node_up.sh
./node_up.sh