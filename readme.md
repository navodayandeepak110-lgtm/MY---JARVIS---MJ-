# 🤖 MY JARVIS(MJ)

[![Python](https://img.shields.io/badge/Python-3.11%20|%203.12%20|%203.13-blue.svg)](https://www.python.org/)
[![AI Engine](https://img.shields.io/badge/Powered%20By-Google%20Gemini%20Live-orange.svg)](https://ai.google.dev/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-brightgreen.svg)](#)

> **MJ** is an Iron Man-inspired, real-time voice and multimodal AI assistant built for desktop. Powered by **Google Gemini Live**, it combines an animated holographic HUD, low-latency conversational audio, computer vision, system automation, and remote mobile control into a single unified assistant.

---

## ✨ Features

- **🎙️ Real-Time Voice Interaction:** Ultra-low latency two-way voice communication via Gemini Live, complete with speech echo cancellation, push-to-talk, and optional local wake word support ("*Hey Jarvis*").
  
- **👤 Holographic 3D Avatar & HUD:** Futuristic Iron Man-style command center with an animated 3D facial mesh rendered in software (PyQt6 + NumPy)—no heavy GPU or OpenGL required. Real-time viseme lip-sync matches speech.
  
- **👁️ Multimodal Vision:** Understands what's happening in real-time through live webcam feeds and screen capture/analysis.
  
- **⚙️ OS & Desktop Control:** Open apps, adjust volume and brightness, control open windows, manage files, and automate repetitive tasks.
  
- **🌐 Web & Browser Automation:** Integrated Playwright web agent for deep searches, automated browser navigation, and live information retrieval.
  
- **📱 Remote Mobile Dashboard:** Built-in FastAPI server allowing you to connect and control MARK-LIV from your smartphone via QR code on your local network.
  
- **🧠 Long-Term Memory & Plugins:** Retains conversation context and user preferences across sessions with an extensible modular plugin system (`plugins/`).

---

## 🚀 Quick Start

### 1. Prerequisites
- **Python 3.11 – 3.13** installed.
- A **Google Gemini API Key** ([Get one from Google AI Studio](https://aistudio.google.com/)).

### 2. Installation

Clone the repository and run the automated setup script:

```bash
-Clone the repository

- Run automated dependency & browser setup
python setup.py
```

> **Note:** `setup.py` automatically detects your operating system, installs required packages, and fetches Playwright browsers.

### 3. Configure API Key

Open `config/api_keys.json` and insert your Gemini API key:

```json
{
  "gemini_api_key": "YOUR_GEMINI_API_KEY_HERE"
}
```

### 4. Launch

Start the assistant:

```bash
python main.py
```

---

## 📂 Project Structure

```text
Mark-LIV/
├── actions/        # Automated action handlers (browser, apps, desktop, vision, system)
├── config/         # System configuration and API credentials (api_keys.json)
├── core/           # Core engine: Gemini client, 3D avatar, audio, visemes, wake-word
├── dashboard/      # FastAPI remote mobile web dashboard & static UI
├── memory/         # Long-term memory manager and config state
├── plugins/        # Extensible custom plugins
├── main.py         # Main entrypoint and event loop
├── ui.py           # PyQt6 holographic HUD and user interface
└── setup.py        # Automated multi-platform installation script
```

---

## ⚙️ Configuration & Controls

- **Push-to-Talk / Voice Mode:** Toggle in settings (⚙) or use the on-screen mic controls.
- **Wake Word:** Opt-in local wake word ("Hey Jarvis") can be downloaded and enabled directly from the in-app settings.
- **Mobile Control:** Click the dashboard icon in the HUD to scan the QR code and connect from your mobile browser.

---

## 📜 License & Credits

- **Creator:** Ayush Kashyap ([@Tecno_techak](https://www.youtube.com/@Tecno_techak/videos))
- **License:** Distributed under the [Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)](LICENSE). Free for personal and educational use.
