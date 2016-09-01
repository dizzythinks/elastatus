from flask import Flask
import os
import yaml
from flask.ext.stormpath import StormpathManager

app = Flask(__name__)
app.secret_key = 'SUPERSECRET' # you should change this to something equally random
app.config['CONFIG_FILE'] = os.path.abspath('app/config.yaml')
configStr = open(app.config['CONFIG_FILE'], 'r')
app.config['CONFIG'] = yaml.load(configStr)
app.config['STORMPATH_API_KEY_FILE'] = app.config['CONFIG']['stormpath']['api_key_file']
app.config['STORMPATH_APPLICATION'] = app.config['CONFIG']['stormpath']['app_name']
app.config['STORMPATH_ENABLE_REGISTRATION'] = False


from views import elastatus as elastatus
app.register_blueprint(elastatus)
