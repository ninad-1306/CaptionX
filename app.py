import os
import uuid
import requests
import base64
import json
from flask import Flask, render_template, request, url_for

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Gemini Vision API setup (updated to gemini-1.5-flash)
GEMINI_API_KEY = GEMINIAPIKEY
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

def get_gemini_caption(image_path, prompt="Describe this image in detail."):
    with open(image_path, "rb") as f:
        image_data = f.read()
    image_b64 = base64.b64encode(image_data).decode("utf-8")
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt},
                    {"inline_data": {"mime_type": "image/jpeg", "data": image_b64}}
                ]
            }
        ]
    }
    response = requests.post(GEMINI_API_URL, json=payload)
    print("Status code:", response.status_code)
    print("Raw response:", response.text)
    try:
        result = response.json()
        if "error" in result:
            return f"API Error: {result['error']['message']}"
        # Parse the caption from the result (depends on Gemini's response format)
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"API Error: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    caption = None
    error = None
    image_url = None
    if request.method == 'POST':
        if 'image' not in request.files:
            error = "No file part"
        else:
            file = request.files['image']
            if file.filename == '':
                error = "No selected file"
            elif file:
                # Save with unique filename
                ext = os.path.splitext(file.filename)[1]
                unique_name = f"{uuid.uuid4().hex}{ext}"
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_name)
                file.save(filepath)
                image_url = url_for('uploaded_file', filename=unique_name)
                try:
                    # Get style from form and build prompt
                    style = request.form.get("style", "detailed")
                    if style == "detailed":
                        prompt = "Describe this image in detail."
                    elif style == "single":
                        prompt = "Write a concise, single-line caption for this image."
                    elif style == "descriptive":
                        prompt = "Write a descriptive caption for this image."
                    elif style == "alt":
                        prompt = (
                            "Generate alt text for this image. "
                            "Only output the alt text itself, with no preamble, explanation, or phrases like 'Alt text:' or 'Here is alt text'."
                        )
                    else:
                        prompt = "Describe this image."
                    caption = get_gemini_caption(filepath, prompt=prompt)
                    # Post-process alt text to remove preambles
                    if style == "alt" and caption:
                        for prefix in [
                            "Alt text:", "Here is alt text for the image:", "Here's alt text for the image:",
                            "Here is the alt text:", "Here is a possible alt text:", "Here is an alt text:"
                        ]:
                            if caption.lower().startswith(prefix.lower()):
                                caption = caption[len(prefix):].strip(" :-")
                except Exception as e:
                    error = f"Error: {e}"
                # Don't delete the image so it can be displayed
    return render_template('index.html', caption=caption, error=error, image_url=image_url)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    from flask import send_from_directory
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True) 