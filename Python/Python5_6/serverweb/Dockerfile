FROM python
ADD server.py .
ADD requirements.txt .
RUN pip install -r  requirements.txt
RUN mkdir ./templates
ADD ./templates/index.html ./templates
ADD ./templates/index2.html ./templates
CMD ["python","./server.py"]
