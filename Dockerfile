FROM python:3.11.4

WORKDIR /word_frequency

COPY word_freq.py /word_frequency/
COPY random_paragraphs.txt /word_frequency/

RUN pip install spacy
RUN python3 -m spacy download en_core_web_sm

CMD [ "python", "./word_freq.py", "./word_frequency/random_paragraphs.txt"]
