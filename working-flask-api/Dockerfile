FROM --platform=linux/amd64 python:3.11 AS build
# FROM python:3.11

RUN python3 -m pip install --upgrade pip

WORKDIR /ws

COPY requirements.txt /ws/

COPY app/ /ws/

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]

# us-central1-docker.pkg.dev/static-bond-416914/arti-repo-for-vertex
# gcloud auth configure-docker us-central1-docker.pkg.dev
# docker build -t us-central1-docker.pkg.dev/static-bond-416914/arti-repo-for-vertex/vertex-service-image-detection:latest .
# docker push us-central1-docker.pkg.dev/static-bond-416914/arti-repo-for-vertex/vertex-service-image-detection:latest

# OR

# gcloud builds submit --region=us-central1 --tag us-central1-docker.pkg.dev/static-bond-416914/arti-repo-for-vertex/vertex-service-image-detection:2

