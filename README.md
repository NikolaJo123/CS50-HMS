This project is intended only for the purpose of studying and it's proposed by Harvard University for accreditation a verified certificate from edX for their CS50's course.

To run this project you need to follow the required steps:

	0. Open command prompt or short cmd.exe
	1. Install Python version 3.8 or above
	2. Install Virtual environment: pip install virtualenv
	3. Create Virtual environment: virtualenv <evnname>
	4. Activate the Virtual environment:
			- Mac OS / Linux: source <evnname>/bin/activate
			- Windows: <evnname>\Scripts\activate
	5. Run pip install -r "requiremetns.txt"/"<Or place the whole path to the location of the requiremetns file.>"
	6. Run python manage.py makemigrations
	7. Run python manage.py migrate
	8. Run python manage.py runsever
	9. After running the above command a text will be printed saying:
			
			"Django version 4.0, using settings 'hospital.settings'
			Starting development server at http://127.0.0.1:8000/
			Quit the server with CTRL-BREAK "
		
	   Copy the http link "http://127.0.0.1:8000/" and past it in a browser and hit enter.
	

After completing all of the above steps you'll successfully run this Django Hospital Management System project.

Additional modules:

	To install Modified Preorder Tree Traversal or short known as MPTT run the following command in cmd.
		
		- pip install django-mptt
	
		MPTT is a technique for storing hierarchical data in a database. The aim is to make retrieval operations very efficient.

	To install Python Pillow run the following command.

		- python -m pip install Pillow

		Pillow or PIL is a Python imaging library that adds image processing capabilities to your Python interpreter. This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities.

