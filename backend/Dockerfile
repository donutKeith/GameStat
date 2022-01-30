#-- Backend Django Image --
FROM python:3.8.3-slim-buster 
#python:alpine3.14
ENV PYTHONUNBUFFERED=1

RUN apt-get update
#RUN apt-get install git

# Add non-root user and create that user's group
RUN addgroup app && useradd -g app -m app
RUN /usr/local/bin/python -m pip install --upgrade pip
#RUN pip install --upgrade pip

# Set the user to app so that everything done from this point
#  on is done by this user and not root
USER app

# Install needed packages and setup non-root user. Use a separate RUN statement to add your own dependencies.
WORKDIR /home/app/app-back
COPY --chown=app:app . .
RUN pip install --use-feature=in-tree-build  .


# Done by docker compose 
#CMD ["python", "manage.py", "runserver", "8050"]
