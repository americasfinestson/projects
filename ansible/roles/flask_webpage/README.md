# flask_webpage

This Ansible role deploys a webpage using the following technologies:
* Python's Flask web framework to create the application
* Apache webserver to host the application
* WSGI to allow Apache to access the Flask application as if it were native
* Docker Compose to deploy the application as a scalable micro service
