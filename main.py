import base64
from flask import Flask, request, render_template
from vertexai.preview.generative_models import GenerativeModel

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    description = "Description will appear here."
    uploaded_image_url = None

    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Save file to static folder
            file_path = f"static/{file.filename}"
            file.save(file_path)
            uploaded_image_url = file_path

            # Convert to Base64
            with open(file_path, "rb") as image_file:
                image_base64 = base64.b64encode(image_file.read()).decode('utf-8')

            # Send to Vertex AI
            description = get_image_description_from_vertex(image_base64)

    return render_template('upload.html', uploaded_image_url=uploaded_image_url, description=description)

def get_image_description_from_vertex(image_base64):
    model = GenerativeModel("gemini-1.5-pro-vision")
    prompt = "وصف تفصيلي للصورة التالية:"
    image = {
        "mime_type": "image/jpeg",  # أو عدل حسب نوع الصورة
        "data": base64.b64decode(image_base64),
    }
    response = model.generate_content([prompt, image])
    return response.text
