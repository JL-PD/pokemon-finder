FROM python:3.10.0rc2-bullseye

#make a directory for our application
WORKDIR /pokemon-finder

#source code
ADD scripts .

#install dependencies
RUN pip install -r requirements.txt

#run the application
CMD ["python", "pokemon_finder.py"]
