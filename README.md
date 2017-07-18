# flask-polymer2-boilerplate
Boilerplate application for a Flask Backend and a Polymer2 Front-End.

## How to use
```bash
$ git clone https://github.com/JunyuMu/flask-polymer2-boilerplate.git
$ cd flask-polymer2-boilerplate/
$ pip install flask
$ npm install -g polymer-cli
```

run in development env
```bash
$ python app.py
```

run in production env
```bash
$ cd static/
$ polymer build
$ cd ..
$ FLASK_ENV="production" python app.py
```

Enjoy.
