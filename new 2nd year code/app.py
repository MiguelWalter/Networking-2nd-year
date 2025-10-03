from flask import Flask, request, render_template, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files.get("file")
        if file and file.filename != "":
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))

    # Get list of all uploaded files
    files = os.listdir(UPLOAD_FOLDER)
    return render_template("index.html", files=files)

@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
