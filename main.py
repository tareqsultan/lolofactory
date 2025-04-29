from flask import Flask, request, render_template_string

app = Flask(__name__)

# نموذج HTML بسيط لرفع صورة
UPLOAD_FORM = '''
<!doctype html>
<title>Upload Image</title>
<h1>Upload an image 📸</h1>
<form method=post enctype=multipart/form-data>
  <input type=file name=image>
  <input type=submit value=Upload>
</form>
{% if filename %}
  <h2>Uploaded Image:</h2>
  <img src="{{ url_for('static', filename=filename) }}" style="max-width:300px;">
  <h2>Description:</h2>
  <p>{{ description }}</p>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filepath = f'static/{file.filename}'
            file.save(filepath)
            # لاحقًا هنا نرسل الصورة إلى Vertex AI ونجيب وصف
            dummy_description = "وصف تجريبي للصورة (سيتم تغييره لاحقًا عبر Vertex AI)"
            return render_template_string(UPLOAD_FORM, filename=file.filename, description=dummy_description)
    return render_template_string(UPLOAD_FORM)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
