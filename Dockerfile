FROM python:3.6

# Copy Requirements to Conatijner and Install the Requirements
COPY . /flask_api
WORKDIR /flask_api
RUN pip install --upgrade pip && pip install Flask==1.0.2

ENTRYPOINT ["python"]
CMD ["flask_app.py"]




