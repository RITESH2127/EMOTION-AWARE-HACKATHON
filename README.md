# 🎭 Emotion-Aware Encryption System

> **Privacy meets AI sentiment analysis** — Encrypt your messages while keeping emotional context visible for moderation and analysis.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-92.7%25-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Backend-black?logo=flask)](https://flask.palletsprojects.com/)

---

## 🚀 Overview

**Emotion-Aware Hackathon** is a proof-of-concept application demonstrating **semantic encryption** — the ability to encrypt message content while preserving emotional sentiment for AI agents, bots, and moderation systems. 

This hackathon project showcases a fascinating intersection of **cryptography** and **natural language processing**: What if moderation systems could flag harmful emotions without violating user privacy? What if end-to-end encrypted chat apps could still detect toxic behavior?

### Key Innovation
- ✅ **Full Message Encryption** using Fernet (symmetric encryption)
- ✅ **Live Emotion Detection** that works on encrypted or plaintext
- ✅ **Multi-emotion Recognition** (e.g., "Joy + Anxiety")
- ✅ **Privacy-Preserving** — Original content stays encrypted
- ✅ **Beautiful UI** with glassmorphism design

---

## 🎬 Live Demo

**[Watch the Testing Video](https://github.com/RITESH2127/EMOTION-AWARE-HACKATHON/raw/main/emotion%20aware%20vidio%20testing%20original.mp4)**

> Click above to see the application in action — encryption, emotion detection, and decryption workflows.

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────┐
│         Frontend (Glassmorphism UI)             │
│    HTML/CSS/JavaScript - Vanilla Stack          │
└────────────────────┬────────────────────────────┘
                     │ API Calls (JSON)
                     ▼
┌─────────────────────────────────────────────────┐
│         Flask Backend API                       │
│  ╔════════════════════════════════════════════╗ │
│  ║  /api/encrypt    → Emotion + Encryption   ║ │
│  ║  /api/decrypt    → Original Message       ║ │
│  ╚════════════════════════════════════════════╝ │
└────────────────────┬────────────────────────────┘
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
   Fernet Key   NRCLex     TextBlob Fallback
   Encryption   Emotions   Sentiment Analysis
```

### Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Flask (Python) |
| **Encryption** | Fernet (cryptography library) |
| **Emotion Detection** | NRCLex + TextBlob with custom keyword mapping |
| **Frontend** | Vanilla HTML/CSS/JavaScript |
| **Key Management** | In-memory storage (demo mode) |

---

## 🎯 How It Works

### 1️⃣ **Encryption Flow**
```
User Input: "I am so incredibly happy, joyful, and excited right now!"
                          ↓
              Emotion Detection Engine
                          ↓
               Emotion Result: "Joy + Excitement"
                          ↓
                   Fernet Encryption
                          ↓
Output: Encrypted text (unreadable) + Visible Emotion Tag
```

### 2️⃣ **Decryption Flow**
```
Encrypted Text + Key
       ↓
   Fernet Decryption
       ↓
Original Message Restored
       ↓
Re-analyze Emotions (verification)
```

### 3️⃣ **Emotion Detection Logic**

The system uses a **multi-layered approach**:

1. **Custom Keyword Mapping** — Fast and accurate for common emotions
   - Joy: `happy, joyful, ecstatic, thrilled, glad, delighted`
   - Anxiety: `anxious, nervous, worried, stress, fear`
   - Sadness: `sad, disappointed, depressed, cry, upset`
   - Anger: `frustrated, angry, mad, hate, rage, furious`
   - Excitement: `excited, can't wait, anticipation, journey`

2. **Combination Detection** — Recognizes multi-emotion patterns
   - "I'm happy but nervous" → `Joy + Anxiety`
   - "Excited yet stressed" → `Excitement + Anxiety`

3. **TextBlob Fallback** — Sentiment polarity analysis for edge cases
   - Polarity > 0.3 → `Joy`
   - Polarity < -0.3 → `Sadness`
   - Otherwise → `Neutral`

---

## 📋 Prerequisites

- **Python 3.8+**
- **pip** (Python package manager)
- **Windows** (for `setup.bat`) **or** Unix-based system (manual setup)

---

## 🚀 Quick Start

### Option 1: Automated Setup (Windows)

```bash
# Clone the repository
git clone https://github.com/RITESH2127/EMOTION-AWARE-HACKATHON.git
cd EMOTION-AWARE-HACKATHON

# Run setup script (installs dependencies + downloads NLTK data)
setup.bat

# Start the Flask server
python app.py
```

The app will be running at: **http://127.0.0.1:5000**

---

### Option 2: Manual Setup (All Platforms)

```bash
# Clone the repository
git clone https://github.com/RITESH2127/EMOTION-AWARE-HACKATHON.git
cd EMOTION-AWARE-HACKATHON

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Download TextBlob/NLTK data
python -m textblob.download_corpora

# Start the server
python app.py
```

Open your browser and navigate to: **http://127.0.0.1:5000**

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `flask` | Web framework for REST API |
| `cryptography` | Fernet encryption/decryption |
| `nrclex` | NRC Emotion Lexicon for emotion detection |
| `textblob` | Sentiment analysis fallback |

See `requirements.txt` for full details.

---

## 🔌 API Reference

### POST `/api/encrypt`

**Request:**
```json
{
  "text": "I am so incredibly happy, joyful, and excited right now!"
}
```

**Response:**
```json
{
  "encrypted_text": "gAAAAABlqX9...[encrypted content]...NKj8=",
  "emotion": "Joy + Excitement",
  "key": "mYi8-BLq_xYZ...[encryption key]...=="
}
```

---

### POST `/api/decrypt`

**Request:**
```json
{
  "encrypted_text": "gAAAAABlqX9...[encrypted content]...NKj8=",
  "key": "mYi8-BLq_xYZ...[encryption key]...=="
}
```

**Response:**
```json
{
  "decrypted_text": "I am so incredibly happy, joyful, and excited right now!",
  "emotion": "Joy + Excitement"
}
```

---

## 🧪 Testing

### Run Emotion Detection Tests

```bash
python test_emotions.py
```

This runs the test suite to verify emotion detection accuracy on various multi-emotion sentences.

### Manual Testing via UI

1. Type a message in the input field
2. Click **"Encrypt"** — See the encrypted text and detected emotion
3. Click **"Decrypt"** — See the original message restored

**Try these test cases:**
- `"I am so happy and excited!"` → Joy + Excitement
- `"I'm nervous but looking forward to this."` → Anxiety + Joy
- `"This is frustrating and makes me sad."` → Anger + Sadness
- `"I don't have strong feelings about this."` → Neutral

---

## 💡 Use Cases

### 1. **Privacy-Preserving Moderation**
Content moderation systems can detect harmful emotions (`Anger`, `Hate`) without reading private messages.

### 2. **Encrypted Mental Health Apps**
Chat apps can detect if users are in distress and suggest resources, without violating encryption.

### 3. **AI Agent Communication**
Bots can understand emotional context in encrypted messages for better, context-aware responses.

### 4. **Workplace Communications**
Internal chat systems can flag hostile/toxic communication patterns while keeping content encrypted.

---

## 🔐 Security Notes

⚠️ **This is a Proof-of-Concept**

- **Key Management**: Keys are stored in-memory for demo purposes. Production deployment requires:
  - Secure key derivation (PBKDF2, Argon2)
  - Key escrow or client-side key management
  - Encrypted key storage
  
- **Encryption**: Uses industry-standard Fernet (AES-128 CBC + HMAC)
- **Emotion Detection**: Works on plaintext during analysis (separate from encrypted storage)

For production use, consider:
- ✅ Client-side encryption (keys never touch the server)
- ✅ Key derivation from user passwords
- ✅ Secure key exchange mechanisms
- ✅ Audit logging for compliance

---

## 📊 Project Statistics

- **Language**: Python (92.7%)
- **Size**: ~3.8 MB
- **License**: MIT
- **Created**: March 7, 2026
- **Status**: Hackathon Proof-of-Concept ✨

---

## 📁 Project Structure

```
EMOTION-AWARE-HACKATHON/
├── app.py                              # Flask backend
├── requirements.txt                    # Python dependencies
├── setup.bat                          # Automated setup (Windows)
├── test_emotions.py                   # Test suite
├── emotion aware vidio testing original.mp4  # Demo video
├── README.md                          # This file
├── LICENSE                            # MIT License
└── templates/
    └── index.html                     # Frontend UI
```

---

## 🎨 Frontend Features

- **Glassmorphism UI** — Modern, frosted-glass aesthetic
- **Real-time Emotion Display** — Color-coded emotion tags
- **Copy-to-Clipboard** — Easy sharing of encrypted content
- **Responsive Design** — Works on desktop & mobile
- **No Framework Dependencies** — Pure HTML/CSS/JavaScript

---

## 🐛 Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'flask'`
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### Issue: `LookupError: NLTK data for textblob not found`
**Solution**: Download TextBlob corpus
```bash
python -m textblob.download_corpora
```

### Issue: Port 5000 already in use
**Solution**: Modify `app.py` line 215
```python
app.run(debug=True, port=5001)  # Use different port
```

### Issue: Video not playing in README
**Solution**: Ensure video file exists at the root directory
```bash
ls -la | grep emotion.*mp4
```

---

## 🤝 Contributing

This is a hackathon project, but contributions are welcome!

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Ideas for Enhancement
- [ ] RSA hybrid encryption (asymmetric + symmetric)
- [ ] User authentication system
- [ ] Database for encrypted message history
- [ ] Advanced emotion classification (more than 5 emotions)
- [ ] Multi-language support
- [ ] Docker containerization
- [ ] Deploy to Heroku/Vercel

---

## 📝 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Ritesh** — Built with ❤️ at the Emotion-Aware Hackathon

- GitHub: [@RITESH2127](https://github.com/RITESH2127)
- Project: [EMOTION-AWARE-HACKATHON](https://github.com/RITESH2127/EMOTION-AWARE-HACKATHON)

---

## ⭐ If You Found This Interesting

Please consider:
- ⭐ **Starring** this repository
- 🐦 **Sharing** on social media
- 💬 **Opening an issue** with suggestions
- 🍴 **Forking** to build upon it

---

## 📚 Resources & References

- [Cryptography Library (Fernet)](https://cryptography.io/en/latest/fernet/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [NRC Emotion Lexicon](https://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm)
- [TextBlob Sentiment Analysis](https://textblob.readthedocs.io/)
- [Semantic Encryption Concept Paper](https://en.wikipedia.org/wiki/Searchable_symmetric_encryption)

---

<div align="center">

**Made with 🎭 + 🔐 + 💻**

*Emotion-Aware Hackathon — Where Privacy Meets Intelligence*

</div>
