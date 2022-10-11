FROM python:3

RUN pip install numpy
RUN pip install sklearn

COPY SVM.pickle SVM.pickle
COPY iris.names iris.names
COPY iris.data iris.data
COPY getPredictions.py getPredictions.py

CMD [ "python", "getPredictions.py" ]