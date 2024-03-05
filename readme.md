# ADOPTERA ETT HUSDJUR

This project is a web application built using Flask. It was created as a part of the Webserverprogramming 1 course during the 23/24 curriculum at NTI Gymnasiet. The website serves as a mock-up of a pet adoption platform, featuring a variety of animals such as dogs, cats, and rabbits that are available for adoption. The application leverages a separate helper.py file for storing pet data and provides distinct routes for users to browse pets by type and view detailed information about individual pets.


## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
- [Acknowledgement](#acknowledgement)
- [License](#license)



## Project Description

"ADOPTERA ETT HUSDJUR" is a web application developed as part of the Webserverprogramming 1 course during the 23/24 curriculum at NTI Gymnasiet. Built using Flask, this project serves as a mock-up of a pet adoption platform.

The application showcases a variety of pets available for adoption, including dogs, cats, and rabbits. The pet data is stored and managed using a separate helper.py file.

The application provides the following routes for user navigation:

- `/`: This route displays the home page, which includes links to different types of pets.
- `/animals/<string:pet_type>`: This route displays a list of all pets of a specified type.
- `/animals/<string:pet_type>/<int:pet_id>`: This route provides detailed information about a specific pet.


## Installation

To install and run the application, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies with the following command:
    ```
    pip install -r requirements.txt
    ```
4. Run the application using the following command:
    ```
    python app.py
    ```
5. Open your web browser and visit `http://localhost:5000` to start using the application.


## Features

- A simulated pet adoption platform designed to mimic real-world applications.
- Features a variety of pets available for adoption, including dogs, cats, and rabbits.
- Utilizes a separate helper.py file for efficient storage and management of pet data.
- Provides distinct, user-friendly routes for browsing pets by type and accessing detailed information about each pet.


## Usage

Once the project is installed and running, you can use it to browse and adopt pets. Here are some examples of how to use the project effectively:

1. Open your web browser and visit `http://localhost:5000`.
2. You will be greeted with the home page, which displays links to different types of pets.
3. Click on a pet type to view a list of all pets of that type.
4. Click on a specific pet to view detailed information about that pet.
5. You can navigate back to the home page or the list of pets by clicking on the corresponding links.

Here is an example code snippet that demonstrates how to fetch all pets of a specific type using the project's API:


## Acknowledgements

This project owes its success to the invaluable contributions of:

- [Gabriel Afram](https://github.com/Gabbeking123) - Whose significant contributions to the core logic were instrumental.

We extend our deepest gratitude to Gabriel Afram and all other contributors who have played a part in this project. Your support has been invaluable. Thank you!


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

