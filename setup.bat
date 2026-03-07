@echo off

echo Install dependencies...

pip install -r requirements.txt



echo.

echo Downloading NLTK tokenizer models (required for NRCLex)...

python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"



echo.

echo Starting Emotion Detect/Encrypt Server...

echo Go to http://127.0.0.1:5000 in your browser!

python app.py

pause

