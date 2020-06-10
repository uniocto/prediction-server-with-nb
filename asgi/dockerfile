FROM jupyter/datascience-notebook:latest
WORKDIR /home/jovyan
COPY model ./
COPY main.ipynb ./
COPY requirements.txt ./
RUN pip install -r requirements.txt
ENTRYPOINT [ "papermill","main.ipynb","out.ipynb"] 