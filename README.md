# Info
This project makes use of youtube-dl to extract info from videos and outputs it in JSON format.

# Requirements
1. AWS account
2. Serverless installed
3. Python (optional)
4. Youtube-DL (optional)

# Install Serverless
`npm install -g serverless`

# Deploy
`serverless deploy`

# Usage
After deploying, you should get a URL back that will serve as the endpoint. Hit it with Postman or curl or whatever. You should get JSON info back.