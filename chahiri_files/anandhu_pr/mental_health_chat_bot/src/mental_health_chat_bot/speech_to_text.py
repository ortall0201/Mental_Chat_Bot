import speech_recognition as sr
import os
from dotenv import load_dotenv
import json
from typing import Optional, Dict, Any

# Load environment variables
load_dotenv()

# Default configuration
DEFAULT_CONFIG = {
    "timeout": 10,  # seconds to wait before giving up
    "phrase_time_limit": 10,  # max seconds for a single phrase
    "energy_threshold": 300,  # minimum audio energy to consider for recording
    "dynamic_energy_threshold": True,  # automatically adjust for ambient noise
    "pause_threshold": 0.8,  # seconds of non-speaking audio before a phrase is considered complete
}


def get_speech_config() -> Dict[str, Any]:
    """Load speech recognition configuration from environment or use defaults."""
    config = DEFAULT_CONFIG.copy()
    
    # Check if there's a config file path in environment
    config_path = os.getenv("SPEECH_CONFIG_PATH")
    if config_path and os.path.exists(config_path):
        try:
            with open(config_path, 'r') as f:
                user_config = json.load(f)
                config.update(user_config)
            print(f"🔧 Loaded speech config from {config_path}")
        except Exception as e:
            print(f"⚠️ Error loading speech config: {e}. Using defaults.")
    
    return config


def setup_credentials() -> bool:
    """Set up Google Cloud credentials for speech recognition."""
    # Check if credentials are already set in environment
    if "GOOGLE_APPLICATION_CREDENTIALS" in os.environ:
        cred_path = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
        if os.path.exists(cred_path):
            return True
    
    # Try to get from .env file
    cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if cred_path and os.path.exists(cred_path):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cred_path
        return True
    
    print("❗ Google Cloud credentials not found or invalid.")
    print("Please set GOOGLE_APPLICATION_CREDENTIALS in your .env file.")
    return False


def recognize_speech_from_mic(config: Optional[Dict[str, Any]] = None) -> Optional[str]:
    """Recognize speech from microphone with enhanced error handling and configurable parameters.
    
    Args:
        config: Optional configuration dictionary to override defaults
        
    Returns:
        Recognized text or None if recognition failed
    """
    # Load configuration
    speech_config = get_speech_config()
    if config:
        speech_config.update(config)
    
    # Ensure credentials are set up
    if not setup_credentials():
        return None
    
    recognizer = sr.Recognizer()
    
    # Apply configuration
    recognizer.energy_threshold = speech_config["energy_threshold"]
    recognizer.dynamic_energy_threshold = speech_config["dynamic_energy_threshold"]
    recognizer.pause_threshold = speech_config["pause_threshold"]
    
    # Initialize microphone
    try:
        mic = sr.Microphone()
    except Exception as e:
        print(f"❗ Error initializing microphone: {e}")
        print("Please check if your microphone is connected and working properly.")
        return None
    
    # Capture audio
    try:
        with mic as source:
            print("🎤 Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(
                source, 
                timeout=speech_config["timeout"],
                phrase_time_limit=speech_config["phrase_time_limit"]
            )
    except sr.WaitTimeoutError:
        print("⏱️ Listening timed out. Please try again.")
        return None
    except Exception as e:
        print(f"❗ Error capturing audio: {e}")
        return None
    
    # Recognize speech
    try:
        print("🧠 Recognizing speech...")
        text = recognizer.recognize_google_cloud(audio)
        print(f"📝 Recognized: {text}")
        return text
    except sr.UnknownValueError:
        print("🤔 Could not understand audio. Please speak clearly.")
        return None
    except sr.RequestError as e:
        print(f"❌ Google Cloud Speech API error: {e}")
        return None
    except Exception as e:
        print(f"❗ Unexpected error during recognition: {e}")
        return None


# Alternative recognition function using Google's free API (as fallback)
def recognize_speech_fallback() -> Optional[str]:
    """Fallback speech recognition using Google's free API."""
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    
    try:
        with mic as source:
            print("🎤 Listening (fallback mode)...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=10)
        
        print("🧠 Recognizing speech (fallback mode)...")
        text = recognizer.recognize_google(audio)  # Using free Google API
        print(f"📝 Recognized: {text}")
        return text
    except Exception as e:
        print(f"❗ Error in fallback recognition: {e}")
        return None
