

"""
FASTAPI + MLOPS – DAY 10
========================

Topic: Deploying Dockerized FastAPI App on AWS EC2

This is the FINAL video of the playlist 🎯

Recap of Previous Work:
- Built ML model (Insurance Premium Prediction)
- Created FastAPI prediction API
- Improved API using best practices
- Dockerized FastAPI app
- Pushed image to Docker Hub

Goal of Day 10:
- Deploy the Docker image on AWS EC2
- Make FastAPI publicly accessible
- Test API & Frontend on cloud
"""

# --------------------------------------------------
# WHAT IS AWS EC2?
# --------------------------------------------------
"""
EC2 (Elastic Compute Cloud) is a virtual server in AWS.

Why EC2?
- Full control
- Easy Docker deployment
- Free-tier available (t2.micro)
"""

# --------------------------------------------------
# STEP 1: CREATE AWS ACCOUNT & EC2 INSTANCE
# --------------------------------------------------
"""
Steps:
1. Create AWS account
2. Go to EC2 Dashboard
3. Launch Instance
4. Choose AMI: Amazon Linux
5. Instance Type: t2.micro (Free Tier)
6. Create key pair (optional)
7. Allow SSH traffic
8. Launch instance
"""

# --------------------------------------------------
# STEP 2: CONNECT TO EC2 INSTANCE
# --------------------------------------------------
"""
Connect using:
- AWS Console (Browser-based terminal)
OR
- SSH using key pair

Once connected, you are inside Linux server.
"""

# --------------------------------------------------
# STEP 3: INSTALL & SETUP DOCKER
# --------------------------------------------------
"""
Run the following commands:

sudo yum update -y
sudo yum install docker -y
sudo service docker start
sudo systemctl enable docker
sudo usermod -aG docker ec2-user
"""

# --------------------------------------------------
# STEP 4: VERIFY DOCKER INSTALLATION
# --------------------------------------------------
"""
Check Docker:
docker --version

Test Docker:
docker run hello-world
"""

# --------------------------------------------------
# STEP 5: PULL DOCKER IMAGE FROM DOCKER HUB
# --------------------------------------------------
"""
Pull your FastAPI image:

docker pull username/fastapi-ml-app
"""

# --------------------------------------------------
# STEP 6: RUN FASTAPI CONTAINER
# --------------------------------------------------
"""
Run container:

docker run -d -p 8000:8000 username/fastapi-ml-app

- -d : detached mode
- -p : port mapping
"""

# --------------------------------------------------
# STEP 7: CONFIGURE AWS SECURITY GROUP
# --------------------------------------------------
"""
VERY IMPORTANT STEP 🚨

Go to:
EC2 → Security Groups → Inbound Rules

Add rule:
- Type: Custom TCP
- Port: 8000
- Source: 0.0.0.0/0

This allows public access to FastAPI.
"""

# --------------------------------------------------
# STEP 8: ACCESS DEPLOYED FASTAPI
# --------------------------------------------------
"""
Find EC2 Public IP address.

Access API:
http://<PUBLIC_IP>:8000/

Swagger Docs:
http://<PUBLIC_IP>:8000/docs

Health Endpoint:
http://<PUBLIC_IP>:8000/health
"""

# --------------------------------------------------
# STEP 9: TEST PREDICTION ENDPOINT
# --------------------------------------------------
"""
POST:
http://<PUBLIC_IP>:8000/predict

Test from Swagger UI or frontend.
"""

# --------------------------------------------------
# STEP 10: CONNECT STREAMLIT FRONTEND
# --------------------------------------------------
"""
Update API URL in Streamlit app:

OLD:
http://localhost:8000/predict

NEW:
http://<PUBLIC_IP>:8000/predict
"""

# --------------------------------------------------
# FINAL RESULT
# --------------------------------------------------
"""
🎉 Congratulations!

You have:
✔ Built ML model
✔ Served it using FastAPI
✔ Dockerized the API
✔ Deployed it on AWS EC2
✔ Connected frontend to cloud API

You are now FULL-STACK ML DEPLOYMENT READY 🚀
"""

# --------------------------------------------------
# END OF PLAYLIST
# --------------------------------------------------
