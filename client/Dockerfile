FROM python
WORKDIR /app
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./
# ENV FLASK_APP "chat-server.py"
ENTRYPOINT ["python3"]
CMD [ "chat-server.py" ]
# CMD [ "-m", "flask", "run", "--host=0.0.0.0", "--port=8080" ]
