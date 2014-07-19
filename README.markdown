#Parrot Client
A open-source, multifunctional Twitter manager

###ParrotFunctionality
####Echoes
Echoes allow a user to schedule a tweet to be posted at a later time

####Squawks
Squawks allow a user to create a collection of tweets which will be posted over a user-designed stretch of time.


###Parrot Client is currently under development.
*  [X]  Establish Twitter connection
*  [X]  Build simple back-end
*  [W]  Build simple front-end
*  [ ]  Create DB
*  [ ]  Support user log-in
*  [ ]  Extend functionality
*  [ ]  UI Improvements


###Usage
Clone.

    git clone https://github.com/imwilsonxu/fbone.git fbone

virtualenv.

    fab setup

Debug.

    fab d

Open `http://127.0.0.1:5000`, done!

## Deploy with WSGI

Clone.

    cd /var/www
    git clone https://github.com/imwilsonxu/fbone.git fbone
    sudo chown `whoami` -R fbone

vhost.

    WSGIDaemonProcess fbone user=wilson group=wilson threads=5
    WSGIScriptAlias /fbone /var/www/fbone/app.wsgi

    <Directory /var/www/fbone/>
        WSGIScriptReloading On
        WSGIProcessGroup fbone
        WSGIApplicationGroup %{GLOBAL}
        Order deny,allow
        Allow from all
    </Directory>

virtualenv.

    fab setup

**IMPORTANT**:

- Change `INSTANCE_FOLDER_PATH` in `fbone/utils.py` to suit yourself.
- Put `production.cfg` under `INSTANCE_FOLDER_PATH`.

## STRUCTURE

    ├── app.wsgi                (mod_wsgi wsgi config)
    ├── CHANGES
    ├── fabfile.py              (fabric file)
    ├── fbone                   (main app)
    │   ├── api                 (api module)
    │   ├── app.py              (create flask app)
    │   ├── config.py           (config module)
    │   ├── decorators.py
    │   ├── extensions.py       (init flask extensions)
    │   ├── frontend            (frontend module)
    │   ├── __init__.py
    │   ├── settings            (settings module)
    │   ├── static
    │   │   ├── css
    │   │   ├── favicon.png
    │   │   ├── humans.txt
    │   │   ├── img
    │   │   ├── js
    │   │   └── robots.txt
    │   ├── templates
    │   │   ├── errors
    │   │   ├── frontend
    │   │   ├── index.html
    │   │   ├── layouts 
    │   │   ├── macros
    │   │   ├── settings
    │   │   └── user
    │   ├── translations        (i18n)
    │   ├── user                (user module)
    │   │   ├── constants.py
    │   │   ├── forms.py        (wtforms)
    │   │   ├── __init__.py
    │   │   ├── models.py
    │   │   ├── views.py
    │   ├── utils.py
    ├── LICENSE
    ├── manage.py               (manage via flask-script)
    ├── MANIFEST.in
    ├── README.markdown
    ├── screenshots
    ├── setup.py
    └── tests                   (unit tests, run via `nosetest`)

## LICENSE

[MIT LICENSE](http://www.tldrlegal.com/license/mit-license)

## ACKNOWLEDGEMENTS

Thanks to Python, Flask, its [extensions](http://flask.pocoo.org/extensions/), and other goodies.
