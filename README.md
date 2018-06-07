Overview
========

This project (Django) will read in a TSV and save Customer and Product models once per line.
An Upload instance is saved and related to the Customers and Products pulled form the TSV. 
The internal product and customer ID's have indices for added performance when querying.
Although I did not end up having time to optimize for large files, the current
function will go through the file one line at a time, without loading the whole
file into memory. The post-upload screen will display whether the upload was 
successful or not.

In an ideal project the upload would kick off a Celery task that would
process the file separately and periodically report back details on parsing 
success/failure which would be relayed via AJAX calls back to the user.

Requirements:
 - Python 3.6
 - Postgres

To Run:

	1. Activate a virtualenv
	2. "pip install -r requirements.txt"
	3. Set the correct DB credentials in atlantic/settings.py
	3. "python manage.py migrate app_atlantic"
	4. "python manage.py runserver 0.0.0.0:8888"
	5. Navigate to http://localhost:8888/atlantic/
	6. Upload an example file