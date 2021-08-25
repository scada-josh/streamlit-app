FROM python:3.9.1
EXPOSE 8501
ADD . /python-streamlit
WORKDIR /python-streamlit
# RUN pip install -r requirements.txt
RUN  pip3 install --upgrade pip && pip3 install -r requirements.txt

# Command overriden by docker-compose
# CMD streamlit run app.py





# Run - Deploy 
ENTRYPOINT ["streamlit", "run", "app.py", "–server.port=8501", "–server.address=0.0.0.0"]
