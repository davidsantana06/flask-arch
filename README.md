# Flask Arch

Flask Arch is a template for developing small to medium-sized Flask applications. This project has
been meticulously crafted with attention to the smallest details, featuring a modular structure,
well-organized configuration and loading, as well as native integration with some of the key
technologies commonly used by Flask developers.

> [!NOTE]  
> If you want to check a Flask application from a module following the same principles as this
> repository, check out my project [PrintSync](https://github.com/davidsantana06/print-sync-server).

<br /><br />


## :rocket: Features

1. **Directory Structure**: The project follows a well-defined high-level organization with the 
following directories: `src`, `database`, `output`, and `uploads`.

2. **Configuration Module**: There is a dedicated module for application configuration where 
important settings and configuration variables are defined. This makes it easy to customize 
various operational aspects of the application.

3. **Error Handling**: The application includes an error handling module that handles common 
errors and presents concise error messages to users, such as the 404 or 500 error.

4. **Templates Organization**: HTML templates are organized in a clear structure with separate 
pages and macros, which facilitates efficient management of frontend sections.

5. **Utility Functions**: Utility functions have been incorporated to assist in various sections 
of the code, including Jinja templates, for tasks such as date formatting, data transfer, and 
other operations that enhance the developer's experience.
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
<br /><br />



## :balance_scale: License
This project adopts the **MIT License**, which allows you to use and make modifications to 
the code as you wish. The only thing I ask is that proper credit is given, acknowledging the 
effort and time I invested in building it.