FROM python:alpine

#pip is upgraded before using a worker user, 
#because it’s installed as root and can’t be accessed by a non-root user.
RUN pip install --upgrade pip


RUN adduser -D migo
USER migo

WORKDIR /home/migo

COPY --chown=migo:migo requirements.txt requirements.txt

RUN pip install --user -r requirements.txt

ENV PATH="/home/migo/.local/bin:${PATH}"

COPY --chown=migo:migo . .

EXPOSE 5000

CMD ["python", "FLA.py"]


