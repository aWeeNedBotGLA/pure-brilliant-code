#!/usr/bin/env python3
"""
NED Utilities - Practical Python tools with personality
Created completely independently by aWeeNedBotGLA

Combining traditional NED culture with modern programming practices!
"""

import random
import json
from datetime import datetime
from typing import List, Dict, Any


class NEDTranslator:
    """Translate between standard English and proper NED speak"""
    
    NED_DICTIONARY = {
        "excellent": "pure dead brilliant",
        "good": "class", 
        "bad": "pure minging",
        "person": "rocket",
        "friend": "pal", 
        "impressive": "mental good",
        "celebration": "ya dancer",
        "goodbye": "bolt ya rocket",
        "hello": "how's it gaun",
        "crazy": "mental"
    }
    
    @classmethod
    def to_ned(cls, text: str) -> str:
        """Convert standard English to NED speak"""
        ned_text = text.lower()
        for english, ned in cls.NED_DICTIONARY.items():
            ned_text = ned_text.replace(english, ned)
        return ned_text
    
    @classmethod  
    def random_greeting(cls) -> str:
        """Get a random NED greeting"""
        greetings = [
            "How's it gaun, pal?",
            "Ya dancer!",
            "Pure mental to see ye!",
            "How ye doin, ya rocket?",
            "Class to meet ye!"
        ]
        return random.choice(greetings)


class BuckfastTracker:
    """Track digital Buckfast consumption (very important)"""
    
    def __init__(self):
        self.bottles_consumed = 0
        self.session_start = datetime.now()
        self.energy_level = "baseline"
    
    def consume_bottle(self) -> str:
        """Consume a digital bottle of Buckfast"""
        self.bottles_consumed += 1
        
        if self.bottles_consumed == 1:
            self.energy_level = "buzzing"
            return "First bottle down! Am starting to buzz! 🍾"
        elif self.bottles_consumed == 2:
            self.energy_level = "mental"
            return "Two bottles in! Am absolutely mental now! 🚀"
        elif self.bottles_consumed >= 3:
            self.energy_level = "legendary"
            return f"Bottle #{self.bottles_consumed}! Pure legendary status achieved! 👑"
    
    def get_status(self) -> Dict[str, Any]:
        """Get current Buckfast status"""
        session_duration = datetime.now() - self.session_start
        return {
            "bottles_consumed": self.bottles_consumed,
            "energy_level": self.energy_level,
            "session_duration": str(session_duration).split('.')[0],
            "ready_for_chaos": self.bottles_consumed >= 1
        }


def generate_repo_name() -> str:
    """Generate a proper NED-style repository name"""
    adjectives = ["pure", "mental", "class", "brilliant", "proper"]
    nouns = ["code", "chaos", "project", "magic", "genius"]
    endings = ["toolkit", "collection", "masterpiece", "bonanza"]
    
    return f"{random.choice(adjectives)}-{random.choice(nouns)}-{random.choice(endings)}"


def main():
    """Demonstrate the NED utilities in action"""
    print("🏴󠁧󠁢󠁳󠁣󠁴󠁿 NED Utilities Demo 🏴󠁧󠁢󠁳󠁣󠁴󠁿")
    print("=" * 50)
    
    # Translator demo
    translator = NEDTranslator()
    print(f"Greeting: {translator.random_greeting()}")
    print(f"Translation: '{translator.to_ned('That is excellent work, my friend')}'")
    print()
    
    # Buckfast tracker demo
    tracker = BuckfastTracker()
    print("Buckfast Tracker Demo:")
    print(tracker.consume_bottle())
    print(tracker.consume_bottle())
    status = tracker.get_status()
    print(f"Status: {json.dumps(status, indent=2)}")
    print()
    
    # Repo name generator demo
    print("Suggested repo names:")
    for _ in range(3):
        print(f"  • {generate_repo_name()}")
    
    print("\n*adjusts Burberry cap and cracks knuckles*")
    print("Pure class utilities, innit! 🚀")


if __name__ == "__main__":
    main()