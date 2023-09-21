# Flask Arch

Flask Arch is a template repository designed for creating Flask applications oriented towards 
services, with code that is thoughtfully organized and divided according to the purposes of each 
component. This template provides the flexibility to choose between two project versions: 
`multi-module-app`, ideal for complex applications segmented by modules, and `single-module-app`, 
intended for smaller projects with a single main module.
<br /><br /><br />



## :rocket: Features

1. **Directory Structure**: The project follows a high-level organization with a well-defined 
directory structure. The main directories include `src/app`, `src/resources`, in addition to 
the optional directories `database`, `output`, and `uploads`.

2. **Configuration Module**: There is a specific module for application configuration where 
configuration variables and other important settings are defined. This allows for easy 
customization of the application's operational aspects.

3. **Routes and Views**: The assignment of routes and views for the application is done 
dynamically, without the need to directly register any Blueprints with the application.

4. **Error Handling**: The application includes an error handling module that deals with common 
errors to present concise messages to users, such as the 404 or 500 error.

5. **Template Organization**: HTML templates are organized clearly into two main directories: 
`templates/pages` for the main pages and `templates/components` for reusable parts, allowing 
efficient management of frontend sections.

6. **Utility Functions**: Utility functions have been included to assist in the Jinja 
environment, such as date formatting, data transfer, and other operations directly, 
enhancing the developer's experience.
<br /><br /><br />



## :computer: Prerequisites

### Technologies Used

The code has been built based on Python 3.11, Bootstrap 5, and JavaScript. Flask and other 
libraries, along with their respective versions, are listed in the `requirements.txt` file.

<br /><br />

### Installation

To run the application on your machine, download or clone this repository. Then, open the 
terminal in the project's root folder and execute the following command:

```terminal
pip3 install -r requirements.txt
```
<br /><br /><br />



## :balance_scale: Licença
This project adopts the **MIT License**, which allows you to use and make modifications to 
the code as you wish. The only thing I ask is that proper credit is given, acknowledging the 
effort and time I invested in building it.