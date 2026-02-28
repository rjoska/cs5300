For this project I used ChatGPT to help me by generating some code and several examples for the structure.
I tried not to overly rely on AI and used the documentation listed, but I did use AI generated code.
The AI generated code was either added in un modified or changed slightly, as for the examples generated they were similar, but
not the same as what the project asked for and I used them to learn as I learn the most by seeing examples and replicating them.
The other use for AI was to help troubleshoot issues like code errors or errors with launching the program.
I had to make some changes to the settings files, and needed to find what files needed to be made (such as urls.py)
and ChatGPT helped either make these files or edit the content within them to work in the DEVEDU enviroment. 
I also used this tutorial https://docs.djangoproject.com/en/6.0/intro/tutorial01/ as a reference. 

Other sources: https://www.django-rest-framework.org/api-guide/testing/, https://docs.djangoproject.com/en/6.0/intro/tutorial03/, https://docs.djangoproject.com/en/6.0/topics/testing/advanced/

HOW TO RUN LOCALLY:
to run the server locally use python3 manage.py runserver 0.0.0.0:3000
then use the nav bar to navigate an parts of the site you wish to see
Features include the movies tab which shows movies, then showings, then seats, after selecting a seat you book it

HOW TO RUN TESTS:
Follow these commands
source homework2/bin/activate
cd cs5300
cd homework2
cd movie_theater_booking
python3 manage.py test (runs both unit and integration tests from tests.py)
behave (runs the behave tests)

HOW TO RUN ON RENDER:
