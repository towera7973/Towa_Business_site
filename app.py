from flask import Flask, render_template, jsonify

app = Flask(__name__)

Projects = [{
    "id": "1",
    "title": "QuardCopter ",
    "description": "Don't bother typing “lorem ipsum” ",
    "image":
    "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Ffree-photos-vectors%2Fbackground&psig=AOvVaw1Z_v7q_Y--lW_8_0DqQYXW&ust=1644415676461000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCIjR_YS_kfQCFQAAAAAdAAAAABAD",
    "link":
    "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Ffree-photos-vectors%2Fbackground&psig=AOvVaw1Z_v7q_Y--lW_8_0DqQYXW&ust=1644415676461000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCIjR_YS_kfQCFQAAAAAdAAAAABAD",
    "tags": ["python", "flask", "html", "css"]
}, {
    "id": "2",
    "title": "Biogas Stove ",
    "description": "into Google translate. If you already tried",
    "image":
    "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Ffree-photos-vectors%2Fbackground&psig=AOvVaw1Z_v7q_Y--lW_8_0DqQYXW&ust=1644415676461000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCIjR_YS_kfQCFQAAAAAdAAAAABAD",
    "link":
    "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Ffree-photos-vectors%2Fbackground&psig=AOvVaw1Z_v7q_Y--lW_8_0DqQYXW&ust=1644415676461000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCIjR_YS_kfQCFQAAAAAdAAAAABAD",
    "tags": ["python", "flask", "html", "css"]
}, {
    "id": "3",
    "title": "IOT PV Voltage moniter ",
    "description": "you may have gotten anything from ",
    "image":
    "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Ffree-photos-vectors%2Fbackground&psig=AOvVaw1Z_v7q_Y--lW_8_0DqQYXW&ust=1644415676461000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCIjR_YS_kfQCFQAAAAAdAAAAABAD",
    "link":
    "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Ffree-photos-vectors%2Fbackground&psig=AOvVaw1Z_v7q_Y--lW_8_0DqQYXW&ust=1644415676461000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCIjR_YS_kfQCFQAAAAAdAAAAABAD",
    "tags": ["python", "flask", "html", "css"]
}]


@app.route("/")
def home_Page():
  return render_template('home.html', projects=Projects)


@app.route("/api/projects")
def get_projects():
  return jsonify(Projects)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
  #app.run(host="0.0.0.0", debug=True, port=5000)
