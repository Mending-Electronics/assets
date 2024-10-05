import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    svg_files = [f for f in os.listdir('static\svg') if f.endswith('.svg')]
    svg_data = []
    for svg_file in svg_files:
        with open(os.path.join('static\svg', svg_file), 'r') as file:
            svg_content = file.read()
            svg_data.append({'name': svg_file.replace(".svg",""), 'content': svg_content})
    return render_template('index.html', svg_data=svg_data)

if __name__ == '__main__':
    app.run(debug=True)
