FROM python:3.9.1
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt 
COPY . /app
CMD streamlit run app.py --server.port $PORT



# gcloud init
# gcloud config set project single-ripsaw-320018

# docker build -t us.gcr.io/single-ripsaw-320018/my-streamlit-app:v1 .
# docker push us.gcr.io/single-ripsaw-320018/my-streamlit-app:v1
# gcloud run deploy --image us.gcr.io/single-ripsaw-320018/my-streamlit-app:v1

# docker build -t us.gcr.io/single-ripsaw-320018/my-streamlit-app:v3 .
# docker push us.gcr.io/single-ripsaw-320018/my-streamlit-app:v3
# gcloud run deploy --image us.gcr.io/single-ripsaw-320018/my-streamlit-app:v3