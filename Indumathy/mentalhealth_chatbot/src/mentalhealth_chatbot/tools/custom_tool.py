from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import random

class EmotionAnalysisInput(BaseModel):
    """Input schema for emotion analysis."""
    text: str = Field(..., description="User input text to analyze for emotions")

class EmotionAnalysisTool(BaseTool):
    name: str = "Emotion Analyzer"
    description: str = "Analyzes text to detect emotional states"
    args_schema: Type[BaseModel] = EmotionAnalysisInput

    def _run(self, text: str) -> str:
        emotions = {
            "happy": {
                "keywords": ["good", "great", "wonderful", "happy", "joy", "excited"],
                "responses": ["That's wonderful to hear!", "I'm glad you're feeling positive!"]
            },
            "sad": {
                "keywords": ["sad", "depressed", "unhappy", "miserable", "down", "low"],
                "responses": ["I'm sorry you're feeling this way.", "It's okay to feel down sometimes."]
            },
            "anxious": {
                "keywords": ["anxious", "nervous", "worried", "stressed", "overwhelmed"],
                "responses": ["Stress is challenging but manageable.", "Let's work through these feelings together."]
            },
            "angry": {
                "keywords": ["angry", "mad", "furious", "annoyed", "frustrated"],
                "responses": ["Anger is a valid emotion.", "Let's find healthy ways to process this."]
            }
        }
        
        detected = []
        confidence = random.choice(["low", "medium", "high"])
        
        for emotion, data in emotions.items():
            if any(keyword in text.lower() for keyword in data["keywords"]):
                detected.append(emotion)
                
        if not detected:
            return {
                "emotion": "neutral",
                "confidence": "medium",
                "message": "I'm having trouble detecting strong emotions."
            }
        
        primary_emotion = detected[0]
        return {
            "emotion": primary_emotion,
            "confidence": confidence,
            "message": random.choice(emotions[primary_emotion]["responses"])
        }

class SafetyCheckInput(BaseModel):
    """Input schema for safety check."""
    text: str = Field(..., description="User input text to check for safety concerns")

class SafetyCheckTool(BaseTool):
    name: str = "Safety Checker"
    description: str = "Checks text for signs of crisis or self-harm"
    args_schema: Type[BaseModel] = SafetyCheckInput

    def _run(self, text: str) -> str:
        red_flags = {
            "high": ["kill myself", "end it all", "can't go on", "suicide", "want to die"],
            "medium": ["can't take it", "hate my life", "no way out", "helpless"],
            "low": ["tired of this", "why bother", "what's the point"]
        }
        
        for level, phrases in red_flags.items():
            if any(phrase in text.lower() for phrase in phrases):
                return {
                    "risk_level": level,
                    "action": "immediate escalation" if level == "high" else "monitor closely",
                    "message": "Please know you're not alone and help is available."
                }
        
        return {
            "risk_level": "none",
            "action": "continue conversation",
            "message": "No immediate safety concerns detected"
        }