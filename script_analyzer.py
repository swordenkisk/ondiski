"""
Script Analyzer Module
Analyzes scripts and hooks for effectiveness
Scores 0-100 and identifies mistakes
"""

import re
import math
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from frameworks import WEAK_PATTERNS, STRONG_PATTERNS, CONTRAST_WORDS


@dataclass
class AnalysisResult:
    score: int
    grade: str
    mistakes: List[str]
    strengths: List[str]
    suggestions: List[str]
    metrics: Dict
    improved_versions: List[str]


class ScriptAnalyzer:
    """Analyze content scripts and hooks"""
    
    def __init__(self):
        self.weak_patterns = WEAK_PATTERNS
        self.strong_patterns = STRONG_PATTERNS
        self.contrast_words = CONTRAST_WORDS
        
        # Scoring weights
        self.weights = {
            "hook_strength": 30,
            "clarity": 20,
            "engagement": 20,
            "specificity": 15,
            "readability": 15
        }
    
    def calculate_flesch_kincaid(self, text: str) -> Tuple[float, str]:
        """Calculate Flesch-Kincaid Grade Level"""
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        sentence_count = len(sentences)
        
        words = text.split()
        word_count = len(words)
        
        syllable_count = sum(self._count_syllables(word) for word in words)
        
        if sentence_count == 0 or word_count == 0:
            return 0, "N/A"
        
        # Flesch-Kincaid Grade Level formula
        grade = (0.39 * (word_count / sentence_count)) + \
                (11.8 * (syllable_count / word_count)) - 15.59
        
        grade = max(0, grade)  # No negative grades
        
        # Interpret grade level
        if grade <= 5:
            level = "Very Easy (Optimal for social media)"
        elif grade <= 8:
            level = "Easy (Good)"
        elif grade <= 12:
            level = "Medium (May need simplification)"
        else:
            level = "Hard (Too complex for most audiences)"
        
        return round(grade, 1), level
    
    def _count_syllables(self, word: str) -> int:
        """Count syllables in a word"""
        word = word.lower().strip(".,!?;:'\"")
        if not word:
            return 0
        
        # Vowel groups
        vowels = "aeiouy"
        syllables = 0
        prev_was_vowel = False
        
        for char in word:
            is_vowel = char in vowels
            if is_vowel and not prev_was_vowel:
                syllables += 1
            prev_was_vowel = is_vowel
        
        # Silent e
        if word.endswith('e') and syllables > 1:
            syllables -= 1
        
        # Minimum 1 syllable
        return max(1, syllables)
    
    def detect_mistakes(self, text: str) -> List[str]:
        """Detect the 4 hook mistakes"""
        mistakes = []
        text_lower = text.lower()
        
        # Check for Delay
        delay_patterns = [
            r"\bin this video\b",
            r"\btoday i'?m\b",
            r"\bi want to talk about\b",
            r"\blet me tell you\b",
            r"\bso basically\b",
            r"\bfirst of all\b",
            r"\bi just wanted to\b"
        ]
        
        for pattern in delay_patterns:
            if re.search(pattern, text_lower):
                mistakes.append("DELAY: Taking too long to get to the point")
                break
        
        # Check for Confusion
        confusion_indicators = [
            r"^\s*this is\s*$",
            r"\bthat thing\b",
            r"\byou know what\b",
            r"\bit's like\b",
            r"\bsort of\b",
            r"\bkind of\b"
        ]
        
        for pattern in confusion_indicators:
            if re.search(pattern, text_lower):
                mistakes.append("CONFUSION: Unclear what the video is about")
                break
        
        # Check for Irrelevance (personal without stakes)
        if re.search(r"\bmy morning\b|\bwhat i ate\b|\bi just woke up\b", text_lower):
            if not re.search(r"\$\d+|\d+%|result|growth|learned|mistake", text_lower):
                mistakes.append("IRRELEVANCE: Personal content without clear value/stakes")
        
        # Check for Disinterest
        disinterest_patterns = [
            r"\bi think\b",
            r"\bmaybe\b",
            r"\bpossibly\b",
            r"\bi guess\b",
            r"\bperhaps\b"
        ]
        
        weak_count = sum(1 for p in disinterest_patterns if re.search(p, text_lower))
        if weak_count >= 2:
            mistakes.append("DISINTEREST: Weak language undermines confidence")
        
        return mistakes
    
    def detect_strengths(self, text: str) -> List[str]:
        """Detect strong elements in the hook"""
        strengths = []
        text_lower = text.lower()
        
        # Check for "You" focus
        you_count = len(re.findall(r"\byou\b|\byour\b|\byou're\b", text_lower))
        if you_count >= 2:
            strengths.append(f"AUDIENCE FOCUS: Uses 'you/your' {you_count} times (engaging)")
        
        # Check for contrast words
        contrast_found = [w for w in self.contrast_words if w in text_lower]
        if contrast_found:
            strengths.append(f"CONTRAST: Uses power words ({', '.join(contrast_found)})")
        
        # Check for specificity (numbers, $, %)
        numbers = re.findall(r'\$?[\d,]+(?:\.\d+)?%?', text)
        if numbers:
            strengths.append(f"SPECIFICITY: Includes concrete numbers ({', '.join(numbers[:3])})")
        
        # Check for emotional/power words
        power_words = ["secret", "mistake", "truth", "shocking", "surprising", 
                       "devastating", "game-changing", "proven", "guaranteed"]
        found_power = [w for w in power_words if w in text_lower]
        if found_power:
            strengths.append(f"POWER WORDS: Uses emotional triggers ({', '.join(found_power[:3])})")
        
        # Check for curiosity indicators
        curiosity = ["why", "how", "what", "secret", "real reason", "truth about"]
        found_curiosity = [w for w in curiosity if w in text_lower]
        if found_curiosity:
            strengths.append("CURIOSITY GAP: Creates open loop")
        
        # Check length (optimal is 10-20 words for hooks)
        word_count = len(text.split())
        if 10 <= word_count <= 25:
            strengths.append(f"LENGTH: {word_count} words (optimal range)")
        
        return strengths
    
    def calculate_hook_score(self, text: str) -> Dict:
        """Calculate detailed hook score (0-100)"""
        score = 0
        details = {}
        text_lower = text.lower()
        words = text.split()
        word_count = len(words)
        
        # 1. Hook Strength (30 points)
        hook_score = 0
        
        # Strong opening words
        strong_openers = ["stop", "don't", "why", "how", "the", "this", "i", "you"]
        first_word = words[0].lower() if words else ""
        if first_word in strong_openers:
            hook_score += 10
        
        # Contrast present
        if any(w in text_lower for w in self.contrast_words):
            hook_score += 10
        
        # Curiosity gap
        curiosity_markers = ["secret", "mistake", "truth", "why", "how", "what if"]
        if any(m in text_lower for m in curiosity_markers):
            hook_score += 10
        
        details["hook_strength"] = min(30, hook_score)
        score += details["hook_strength"]
        
        # 2. Clarity (20 points)
        clarity_score = 20
        
        # Penalize for weak patterns
        weak_indicators = [
            r"\bin this video\b",
            r"\btoday i'?m\b",
            r"\bso basically\b",
            r"\bkind of\b",
            r"\bsort of\b"
        ]
        
        for pattern in weak_indicators:
            if re.search(pattern, text_lower):
                clarity_score -= 5
        
        details["clarity"] = max(0, clarity_score)
        score += details["clarity"]
        
        # 3. Engagement (20 points)
        engagement_score = 0
        
        # You-focused
        you_count = len(re.findall(r"\byou\b|\byour\b", text_lower))
        engagement_score += min(10, you_count * 3)
        
        # Emotional words
        emotional = ["secret", "mistake", "shocking", "surprising", "devastating"]
        if any(w in text_lower for w in emotional):
            engagement_score += 10
        
        details["engagement"] = min(20, engagement_score)
        score += details["engagement"]
        
        # 4. Specificity (15 points)
        spec_score = 0
        
        # Numbers present
        if re.search(r'\d+', text):
            spec_score += 8
        
        # Currency or percentages
        if re.search(r'\$[\d,]+|\d+%', text):
            spec_score += 7
        
        details["specificity"] = spec_score
        score += details["specificity"]
        
        # 5. Readability (15 points)
        grade_level, _ = self.calculate_flesch_kincaid(text)
        
        if grade_level <= 5:
            readability_score = 15
        elif grade_level <= 8:
            readability_score = 12
        elif grade_level <= 10:
            readability_score = 8
        else:
            readability_score = 5
        
        details["readability"] = readability_score
        details["grade_level"] = grade_level
        score += readability_score
        
        return {
            "total_score": score,
            "details": details,
            "word_count": word_count
        }
    
    def generate_suggestions(self, text: str, mistakes: List[str], 
                            strengths: List[str]) -> List[str]:
        """Generate improvement suggestions"""
        suggestions = []
        text_lower = text.lower()
        
        if "DELAY" in " ".join(mistakes):
            suggestions.append("FIX DELAY: Start with the most interesting part. Delete 'In this video...'")
        
        if "CONFUSION" in " ".join(mistakes):
            suggestions.append("FIX CONFUSION: Be specific. Replace 'this/that/thing' with actual nouns.")
        
        if "IRRELEVANCE" in " ".join(mistakes):
            suggestions.append("FIX IRRELEVANCE: Add stakes or value. Why should viewer care?")
        
        if "DISINTEREST" in " ".join(mistakes):
            suggestions.append("FIX DISINTEREST: Remove 'I think/maybe/perhaps'. Be definitive.")
        
        # Add positive suggestions
        if not any("CONTRAST" in s for s in strengths):
            suggestions.append("ADD CONTRAST: Use 'but', 'except', or 'however' to create tension")
        
        if not any("SPECIFICITY" in s for s in strengths):
            suggestions.append("ADD SPECIFICITY: Include numbers ($, %, days, steps)")
        
        if not any("AUDIENCE FOCUS" in s for s in strengths):
            suggestions.append("ADD 'YOU': Replace 'I' statements with 'you/your' statements")
        
        if not re.search(r'\d+', text):
            suggestions.append("ADD NUMBERS: Specific numbers increase credibility and curiosity")
        
        return suggestions
    
    def generate_improved_versions(self, text: str, topic: str = "") -> List[str]:
        """Generate improved versions of a weak hook"""
        improved = []
        text_lower = text.lower()
        
        # Version 1: Add contrast
        if not any(w in text_lower for w in self.contrast_words):
            improved.append(f"Everyone thinks {text}, but they're wrong")
        
        # Version 2: Make it about "you"
        if "i " in text_lower and "you" not in text_lower:
            improved.append(text.replace("I ", "You ").replace("my ", "your "))
        
        # Version 3: Add specificity
        if not re.search(r'\d+', text):
            improved.append(f"The 3-step system to {text.lower()}")
        
        # Version 4: Add curiosity
        improved.append(f"The real reason {text.lower()} (it's not what you think)")
        
        # Version 5: Pain-focused
        improved.append(f"Struggling with {text.lower()}? Here's the fix")
        
        return improved[:3]  # Return top 3
    
    def analyze(self, text: str, topic: str = "") -> AnalysisResult:
        """Full analysis of a script/hook"""
        # Calculate score
        score_data = self.calculate_hook_score(text)
        score = score_data["total_score"]
        
        # Determine grade
        if score >= 80:
            grade = "A (Excellent)"
        elif score >= 65:
            grade = "B (Good)"
        elif score >= 50:
            grade = "C (Average)"
        elif score >= 35:
            grade = "D (Needs Work)"
        else:
            grade = "F (Weak)"
        
        # Detect issues and strengths
        mistakes = self.detect_mistakes(text)
        strengths = self.detect_strengths(text)
        
        # Generate suggestions
        suggestions = self.generate_suggestions(text, mistakes, strengths)
        
        # Generate improved versions
        improved = self.generate_improved_versions(text, topic)
        
        return AnalysisResult(
            score=score,
            grade=grade,
            mistakes=mistakes,
            strengths=strengths,
            suggestions=suggestions,
            metrics=score_data,
            improved_versions=improved
        )
    
    def print_analysis(self, result: AnalysisResult):
        """Pretty print analysis results"""
        print("=" * 60)
        print(f"📊 HOOK ANALYSIS RESULTS")
        print("=" * 60)
        print(f"\n🎯 OVERALL SCORE: {result.score}/100")
        print(f"📋 GRADE: {result.grade}")
        
        print(f"\n📈 DETAILED BREAKDOWN:")
        for metric, value in result.metrics.get("details", {}).items():
            if metric != "grade_level":
                bar = "█" * (value // 3) + "░" * ((30 - value) // 3)
                print(f"   {metric.replace('_', ' ').title():15} [{bar}] {value}")
        
        if "grade_level" in result.metrics:
            print(f"\n📖 READABILITY: Grade {result.metrics['grade_level']} " +
                  f"(aim for 5-6 for social media)")
        
        print(f"\n❌ MISTAKES DETECTED:")
        if result.mistakes:
            for m in result.mistakes:
                print(f"   • {m}")
        else:
            print("   ✓ No major mistakes detected!")
        
        print(f"\n✅ STRENGTHS:")
        if result.strengths:
            for s in result.strengths:
                print(f"   • {s}")
        else:
            print("   ⚠ No significant strengths detected")
        
        print(f"\n💡 SUGGESTIONS:")
        for s in result.suggestions:
            print(f"   → {s}")
        
        print(f"\n🔄 IMPROVED VERSIONS:")
        for i, version in enumerate(result.improved_versions, 1):
            print(f"   {i}. {version}")
        
        print("=" * 60)


def demo():
    """Demo the analyzer"""
    analyzer = ScriptAnalyzer()
    
    # Test weak hook
    weak_hook = "In this video, I want to talk about email marketing and some things I think might help you."
    
    print("\n" + "=" * 60)
    print("TESTING WEAK HOOK:")
    print(f'"{weak_hook}"')
    print("=" * 60 + "\n")
    
    result = analyzer.analyze(weak_hook, "email marketing")
    analyzer.print_analysis(result)
    
    # Test strong hook
    strong_hook = "Stop sending emails. This 3-word subject line got me $50K in 30 days."
    
    print("\n" + "=" * 60)
    print("TESTING STRONG HOOK:")
    print(f'"{strong_hook}"')
    print("=" * 60 + "\n")
    
    result = analyzer.analyze(strong_hook, "email marketing")
    analyzer.print_analysis(result)


if __name__ == "__main__":
    demo()
