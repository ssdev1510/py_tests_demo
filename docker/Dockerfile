FROM python:3.8-slim-buster
#RUN pip install pytest
WORKDIR /demo
COPY . .
RUN pip install -r docker/requirements.txt
CMD [ "pytest","-v","package/pytest_demo.py"]