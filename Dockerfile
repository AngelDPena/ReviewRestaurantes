FROM python:3.10.2

RUN mkdir /ReviewRestaurantes

RUN pip install pipenv
RUN pip install maskpass
RUN pip install pymongo
RUN pip install python-decouple

ENV MONGODB_CONNECTION_STRING="mongodb+srv://Angel:ycMVTPw6PNkHm1iy@cluster0.oqicaw7.mongodb.net/test"

ADD main.py /ReviewRestaurantes 

WORKDIR /ReviewRestaurantes

ENTRYPOINT [ "python" ]
CMD [ "main.py" ]
