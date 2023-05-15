FROM python:3.10-slim-buster

USER root

WORKDIR /app/

COPY . .

RUN python -m venv venv

RUN . venv/bin/activate

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

USER 1001

ENTRYPOINT ["streamlit"]

CMD ["run", "app.py"]