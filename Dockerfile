FROM python:latest
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /food_planner
COPY requirements.txt /food_planner/
RUN pip install -r requirements.txt
COPY . /food_planner/

CMD ["sh", "ops/backend_start.sh"]