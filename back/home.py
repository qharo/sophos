from flask import Flask, render_template
import os

#---CHANGING THE TEMPLATE DIRECTORY---#
main_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
temp_dir = os.path.join(os.path.join(main_dir, 'front'), 'templates')
print(temp_dir)
#--------------#


#---RUNNING APP---#
app = Flask(__name__, template_folder=temp_dir)
#--------------#
word = 'JAS CHKING'

@app.route("/")
def home():
    return render_template('index.html', name=word)

if __name__ == "__main__":
    app.run()