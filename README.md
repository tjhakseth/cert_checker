# Certificate Checker

## Getting Started (Contributing)
### Dev Environment
The app is written in python 2.7, if you are using a mac it comes pre-installed otherwise 
you may need to download it (will not work with python 3).

Go to the directory where you would like to copy the repo and enter: </br>
<code>git clone https://github.com/tjhakseth/cert_checker.git</code>

Once cloning is done, cd into <tt>mysite</tt> and create a 
virtual environment.

If you already do not have  virtualenv installed yet get it with (good 
guide <a href = http://docs.python-guide.org/en/latest/dev/virtualenvs/ >
here</a>):</br>
<code>pip install virtualenv </code>

Then create your virtual environment: </br>
<code>virtualenv env</code> </br>
And enter it with:</br>
<code>source env/bin/activate</code>

Now install all the needed packages with: </br>
<code>pip install -r requirements.txt</code>

Now you should be good to go!

### Running the app
cd into <tt>mysite</tt> 

Then enter:
<code>python manage.py runserver </code>

The app should now be available at <tt>http://127.0.0.1:8000/</tt>.