"""
A Flask application for adopting pets.

This module provides routes for displaying the home page, a list of pets based on pet type, and details about a specific pet.

Example:
  To run the application, use the following command:
    python app.py

Attributes:
  app (Flask): The Flask application object.

"""

from flask import Flask
from helper import pets

app = Flask(__name__)


@app.route('/')
def index():
  """
  Returns the HTML content for the index page.

  Returns:
    str: The HTML content for the index page.
  """
  return '''
  <h1>Adopt a Pet<h1/>
  <p>Browse through the links below to find your new furry friend:<p/> 
  <ul>
  <li><a href='/animals/dogs'>Dogs</a></li> 
  <li><a href='/animals/cats'>Cats </a> </li> 
  <li><a href='/animals/rabbits'>Rabbits</a></li> 
  </ul>
  '''


@app.route('/animals/<string:pet_type>')
def animals(pet_type):
  """
  Displays a list of all pets of the specified type.

  Args:
    pet_type (str): The type of pet to display.

  Returns:
    str: The HTML content for the list of pets.

  """
  html = f'<h1>List of {pet_type}<h1/>'
  html += '<ul>'
  for id, pet in enumerate(pets[pet_type]):
    html += f'<li><a href="/animals/{pet_type}/{id}">{pet["name"]}</a></li>'
  return html


@app.route('/animals/<string:pet_type>/<int:pet_id>')
def pet(pet_id, pet_type):
  """
  Displays details about a specific pet.

  Args:
    pet_id (int): The ID of the pet to display.
    pet_type (str): The type of pet to display.

  Returns:
    str: The HTML content with the details of the specified pet.

  """
  list_pet_type = pets[pet_type]
  pet = list_pet_type[pet_id]
  return f'''
  <h1> {pet["name"]}</h1>

  <img src={pet["url"]} /> 

  <p>{pet["description"]}</p>

  <ul>
    <li>{pet["breed"]} </li>
    <li>{pet["age"]} </li>
  </ul>

  '''


app.run(debug=True, host="0.0.0.0")
