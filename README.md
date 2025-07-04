# 🖼️ CaptionX - Gemini Vision Web App

A minimal, modern web app for generating AI-powered image captions using Google Gemini Vision (Gemini 1.5 Flash). Supports multiple caption styles, including detailed, single-line, descriptive, and accessibility-focused alt text.

---

## 🚀 Features
- **Image Upload**: Drag & drop or browse to upload images
- **AI-Powered Captions**: Uses Gemini Vision API for high-quality captions
- **Caption Styles**: Choose from Detailed, Single line, Descriptive, or Accessibility (alt text)
- **Beautiful UI**: Clean, responsive, and easy to use
- **No local AI models required**: All processing is done via Gemini API

---

## 🛠️ Setup

### 1. Clone the repository
```bash
# If you haven't already
cd /path/to/your/project
```

### 2. Install dependencies
```bash
pip install flask requests
```

### 3. Add your Gemini API key
- Your API key is set in `app.py` as `GEMINI_API_KEY`.
- Get your key from [Google AI Studio](https://aistudio.google.com/app/apikey) or your Google Cloud Console.

### 4. Run the app
```bash
python app.py
```

### 5. Open in your browser
Go to [http://localhost:5000](http://localhost:5000)

---

## 🎨 Usage
1. **Choose a caption style** from the dropdown (e.g., Detailed, Single line, Descriptive, Accessibility).
2. **Upload an image** (JPG, PNG, etc.).
3. **Click "Generate Caption"**.
4. **View and copy** the generated caption.

---

## 📝 Caption Styles
- **Detailed**: A rich, in-depth description of the image
- **Single line**: A concise, one-line caption
- **Descriptive**: A clear, informative caption
- **Accessibility (alt text)**: Alt text for screen readers (no preamble, just the description)

---

## ⚡ Customization
- **Add more styles**: Edit the dropdown in `templates/index.html` and the prompt logic in `app.py`.
- **Change UI**: Edit `templates/index.html` for layout, colors, etc.
- **Change API key**: Update `GEMINI_API_KEY` in `app.py`.

---

## 🛡️ Security & Privacy
- Images are only sent to the Gemini API for captioning and are not stored long-term.
- **Do not share your API key publicly.**

---

## 🧩 Dependencies
- Python 3.8+
- Flask
- Requests

---

## 🙏 Acknowledgments
- [Google Gemini API](https://ai.google.dev/)
- [Flask](https://flask.palletsprojects.com/)

---

**Built with ❤️ for accessible, AI-powered image captioning!** 