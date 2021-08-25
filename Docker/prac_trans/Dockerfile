FROM python:alpine

RUN pip install --upgrade pip

RUN adduser -D migo
USER migo

WORKDIR /home/migo

COPY --chown=migo:migo requirements.txt requirements.txt

RUN pip install --user -r requirements.txt

ENV PATH="/home/migo/.local/bin:{$PATH}"
ENV PATH="/bin:{$PATH}"

COPY --chown=migo:migo . .


CMD ["python","web.py"]  
#Use " instead of ' in CMD. 