"""
FASTAPI + MLOPS – DAY 9
=======================

Topic: Docker Basics (from CampusX)

Chapters Covered:
1. What is Docker?
2. Need for Docker
3. How Docker is Used
4. Docker Engine
5. Docker Image
6. Dockerfile
7. Docker Container
8. Docker Registry
9. Docker Lifecycle
10. Use-Cases
11. Setup & Verification
12. Dockerizing a Flask App
13. Pushing Image to Docker Hub

--------------------------------------------------
WHAT IS DOCKER?
--------------------------------------------------
Docker is a containerization platform.

It allows us to package:
- Application
- Dependencies
- Environment

into a single unit called a CONTAINER.

"Runs everywhere the same way"
"""

# --------------------------------------------------
# NEED FOR DOCKER
# --------------------------------------------------
"""
Problems without Docker:
- Works on my machine issue
- Dependency conflicts
- Difficult deployment
- Environment mismatch

Docker solves this by:
- Isolating apps
- Making deployments reproducible
- Simplifying DevOps
"""

# --------------------------------------------------
# HOW DOCKER IS USED?
# --------------------------------------------------
"""
Developer -> Dockerfile -> Docker Image -> Docker Container

You:
1. Write Dockerfile
2. Build Image
3. Run Container
"""

# --------------------------------------------------
# DOCKER ENGINE
# --------------------------------------------------
"""
Docker Engine components:
1. Docker Client
2. Docker Daemon
3. REST API

Client -> Daemon -> Container
"""

# --------------------------------------------------
# DOCKER IMAGE
# --------------------------------------------------
"""
Docker Image:
- Read-only template
- Blueprint of application
- Created from Dockerfile

Example:
python:3.10
"""

# --------------------------------------------------
# DOCKERFILE
# --------------------------------------------------
"""
Dockerfile is a text file containing instructions
to build an image.

Common instructions:
FROM
WORKDIR
COPY
RUN
EXPOSE
CMD
"""

# --------------------------------------------------
# DOCKER CONTAINER
# --------------------------------------------------
"""
Container:
- Running instance of image
- Lightweight
- Isolated

Image -> Container
"""

# --------------------------------------------------
# DOCKER REGISTRY
# --------------------------------------------------
"""
Registry stores Docker images.

Popular registries:
- Docker Hub
- AWS ECR
- Google Artifact Registry
"""

# --------------------------------------------------
# DOCKER LIFECYCLE
# --------------------------------------------------
"""
Docker Lifecycle:
Dockerfile -> Image -> Container -> Stop -> Remove
"""

# --------------------------------------------------
# DOCKER USE CASES
# --------------------------------------------------
"""
- Deploy FastAPI apps
- Deploy ML models
- CI/CD pipelines
- Microservices
- Cloud deployments
"""

# --------------------------------------------------
# SETUP & VERIFY DOCKER
# --------------------------------------------------
"""
Install Docker:
https://www.docker.com/products/docker-desktop/

Verify installation:
docker --version
docker run hello-world
"""

# --------------------------------------------------
# DOCKERIZING A FLASK APP (EXAMPLE)
# --------------------------------------------------
"""
Example Flask App: app.py

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Docker"

app.run(host="0.0.0.0", port=5000)
"""

# --------------------------------------------------
# DOCKERFILE FOR FLASK APP
# --------------------------------------------------
"""
Dockerfile

FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]
"""

# --------------------------------------------------
# BUILD & RUN IMAGE
# --------------------------------------------------
"""
Build image:
docker build -t flask-app .

Run container:
docker run -p 5000:5000 flask-app
"""

# --------------------------------------------------
# PUSH IMAGE TO DOCKER HUB
# --------------------------------------------------
"""
Login:
docker login

Tag image:
docker tag flask-app username/flask-app

Push image:
docker push username/flask-app
"""

# --------------------------------------------------
# END OF DAY 9
# --------------------------------------------------
"""
You are now Docker-ready 🚀
"""

