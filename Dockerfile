FROM python:3.12-slim
WORKDIR /docker_deploy/
COPY ./app.py /docker_deploy/
COPY ./model.pkl /docker_deploy/
COPY ./model_predictions.py /docker_deploy/
COPY ./model_run.py /docker_deploy/
COPY ./requirements.txt /docker_deploy/
RUN pip install -r /docker_deploy/requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]