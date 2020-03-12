#!/bin/sh

# install software prerequisites.
yum install -y git
easy_install flask

# Clone the code from github.
git clone https://github.com/georgeoh/FlaskDirectUploader

#initialize enviroment variables.
export AWS_ACESS_KEY_ID=
export AWS_SECRET_ACESS_KEY=
export S3_BUCKET=usernamegoeshere

#Run server
cd FLaskDirectUploader
python deploymentaws.py