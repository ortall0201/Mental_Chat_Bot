# Speech Recognition Module Documentation

## Overview

The enhanced speech recognition module provides robust speech-to-text capabilities for the Mental Health Chat Bot. It features:

- Configurable parameters for speech recognition
- Comprehensive error handling
- Fallback recognition using Google's free API
- Proper credential management

## Setup

### 1. Google Cloud Credentials

To use the Google Cloud Speech-to-Text API:

1. Create a Google Cloud project and enable the Speech-to-Text API
2. Create a service account and download the JSON key file
3. Add the path to your credentials file in your `.env` file:

```
GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/service-account-file.json
```

### 2. Configuration

The speech recognition module can be configured using a JSON file. Create a file at `config/speech_config.json` with your desired settings or use the provided sample.

Add the path to your configuration file in your `.env` file:

```
SPEECH_CONFIG_PATH=/path/to/config/speech_config.json
```

## Configuration Options

The following parameters can be configured:

| Parameter | Description | Default |
|-----------|-------------|--------|
| `timeout` | Seconds to wait before giving up | 10 |
| `phrase_time_limit` | Max seconds for a single phrase | 10 |
| `energy_threshold` | Minimum audio energy to consider for recording | 300 |
| `dynamic_energy_threshold` | Automatically adjust for ambient noise | true |
| `pause_threshold` | Seconds of non-speaking audio before a phrase is considered complete | 0.8 |
| `fallback_to_google_free` | Whether to use Google's free API as fallback | true |

## Usage

```python
from src.mental_health_chat_bot.speech_to_text import recognize_speech_from_mic, recognize_speech_fallback

# Basic usage
text = recognize_speech_from_mic()

# With custom configuration
config = {
    "timeout": 15,
    "phrase_time_limit": 20
}
text = recognize_speech_from_mic(config)

# Fallback to free API
text = recognize_speech_fallback()
```

## Error Handling

The module handles various error scenarios:

- Microphone initialization errors
- Timeout errors
- Speech recognition errors
- API request errors
- Credential errors

Each error type is handled appropriately with informative error messages.

## Troubleshooting

1. **No sound detected**: Check your microphone connection and permissions
2. **API errors**: Verify your Google Cloud credentials are valid and the API is enabled
3. **Recognition issues**: Try adjusting the energy threshold or speaking more clearly
4. **Timeout errors**: Increase the timeout value in the configuration

## Dependencies

- `speech_recognition`: Core speech recognition functionality
- `dotenv`: Environment variable management
- `json`: Configuration file parsing