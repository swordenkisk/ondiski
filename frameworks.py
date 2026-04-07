"""
Content Strategy Frameworks
Extracted from 11 expert video transcripts
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
import random

@dataclass
class Framework:
    name: str
    source: str
    description: str
    components: List[str]
    examples: List[str]

# =============================================================================
# FRAMEWORK 1: 4 Hook Mistakes (Callaway)
# =============================================================================
HOOK_MISTAKES = Framework(
    name="4 Hook Mistakes",
    source="Callaway",
    description="The four critical mistakes that kill hook performance",
    components=[
        "Delay - Taking too long to get to the point",
        "Confusion - Unclear what the video is about",
        "Irrelevance - Doesn't match viewer intent",
        "Disinterest - Fails to create curiosity gap"
    ],
    examples=[
        "❌ Delay: 'In this video, I'm going to talk about...'",
        "❌ Confusion: 'The thing about that is...' (what thing?)",
        "❌ Irrelevance: Clickbait that doesn't deliver",
        "❌ Disinterest: 'Here's my morning routine' (no stakes)"
    ]
)

# =============================================================================
# FRAMEWORK 2: 3-Step Hook Formula (Callaway)
# =============================================================================
THREE_STEP_HOOK = Framework(
    name="3-Step Hook Formula",
    source="Callaway",
    description="Context Lean → Scroll Stop → Contrarian Snapback",
    components=[
        "Context Lean - Establish familiar ground quickly",
        "Scroll Stop - Pattern interrupt or curiosity gap",
        "Contrarian Snapback - Challenge expectation with 'but', 'except', 'here's why'"
    ],
    examples=[
        "✓ 'Everyone says email marketing is dead, but I just made $50K from one email'",
        "✓ 'You think you need more followers? Here's why that's killing your growth'",
        "✓ 'This common advice sounds smart, except it destroyed my business'"
    ]
)

# =============================================================================
# FRAMEWORK 3: 6-Stage Psychology (Callaway)
# =============================================================================
SIX_STAGE_PSYCHOLOGY = Framework(
    name="6-Stage Psychology",
    source="Callaway",
    description="The psychological journey from pain to action",
    components=[
        "Pain - Identify the problem (agitate)",
        "Trust - Establish credibility quickly",
        "Plan - Show the solution path",
        "Likability - Build connection/relatability",
        "Attention - Maintain with pattern interrupts",
        "Action - Clear CTA with low friction"
    ],
    examples=[
        "Pain: 'Struggling to get views? You're not alone...'",
        "Trust: 'I've grown 5 channels to 100K+ using this'",
        "Plan: 'Here's the 3-step system that works'",
        "Likability: 'I made all the mistakes so you don't have to'",
        "Attention: *Visual change* 'But wait, there's a catch'",
        "Action: 'Comment HOOK and I'll send you the template'"
    ]
)

# =============================================================================
# FRAMEWORK 4: 5 Storytelling Techniques (Video 5)
# =============================================================================
FIVE_STORY_TECHNIQUES = Framework(
    name="5 Storytelling Techniques",
    source="Video 5 Analysis",
    description="Elements that make stories engaging and memorable",
    components=[
        "Location - Ground the story in a specific place",
        "Action - Show, don't just tell",
        "Thought - Reveal internal dialogue",
        "Emotion - Connect through feelings",
        "Dialogue - Use direct quotes/conversations"
    ],
    examples=[
        "Location: 'I was sitting in my car, engine running...'",
        "Action: 'I slammed the laptop shut and stared at the $0 balance'",
        "Thought: 'I remember thinking, this is never going to work'",
        "Emotion: 'I felt this pit in my stomach, like I'd failed everyone'",
        "Dialogue: 'My wife looked at me and said, \"Just one more month\"'"
    ]
)

# =============================================================================
# FRAMEWORK 5: Video Structure (Jessica Stansberry)
# =============================================================================
VIDEO_STRUCTURE = Framework(
    name="Video Structure",
    source="Jessica Stansberry",
    description="The 4-part structure for engaging videos",
    components=[
        "Hook - First 3 seconds, stop the scroll",
        "Intro - 10-15 seconds, set expectations",
        "Meat - The valuable content (bulk of video)",
        "Outro - CTA and next steps"
    ],
    examples=[
        "Hook: 'I lost everything. Here's what I learned.'",
        "Intro: 'In this video, I'll show you the exact 3-step process'",
        "Meat: Detailed breakdown with examples and proof",
        "Outro: 'If this helped, subscribe and grab my free guide below'"
    ]
)

# =============================================================================
# FRAMEWORK 6: Shorts Formula (Jenny Hoyos)
# =============================================================================
SHORTS_FORMULA = Framework(
    name="Shorts Formula",
    source="Jenny Hoyos",
    description="Optimization tactics for short-form content",
    components=[
        "34-second optimization - Sweet spot for retention",
        "Visual hooks - Change scene every 1.7 seconds",
        "Text overlays - Reinforce key points visually",
        "Pattern interrupts - Keep attention with cuts/zooms",
        "Loop potential - End that connects to beginning"
    ],
    examples=[
        "34s: 'The fastest way to [result] in 30 seconds'",
        "Visual: Cut to reaction, cut to demonstration, cut to result",
        "Text: 'Mistake #1' → 'Mistake #2' → 'The Fix'",
        "Loop: 'And that's how you... wait, there's one more thing'"
    ]
)

# =============================================================================
# FRAMEWORK 7: Retention Tactics (Video 11)
# =============================================================================
RETENTION_TACTICS = Framework(
    name="Retention Tactics",
    source="Video 11 Analysis",
    description="Techniques to keep viewers watching longer",
    components=[
        "2-second shot changes - Prevents scroll behavior",
        "Pattern interrupts - Visual/audio changes every 3-5 seconds",
        "Open loops - Promise payoff later in video",
        "Curiosity gaps - 'The reason why will shock you'",
        "Stakes escalation - Increase tension throughout"
    ],
    examples=[
        "2s rule: Never stay on same shot for more than 2 seconds",
        "Pattern: Zoom in, B-roll, text popup, face closeup",
        "Open loop: 'At the end, I'll reveal the mistake that cost me $10K'",
        "Curiosity: 'The real reason isn't what you think'",
        "Stakes: 'And it gets worse... then even worse...'"
    ]
)

# =============================================================================
# FRAMEWORK 8: CTA Framework (Exposure Ninja)
# =============================================================================
CTA_FRAMEWORK = Framework(
    name="CTA Framework",
    source="Exposure Ninja",
    description="Call-to-action that converts",
    components=[
        "High value - What's in it for them?",
        "Low risk - Remove friction and fear",
        "Sales alignment - Match buyer journey stage",
        "Urgency/scarcity - Reason to act now",
        "Single action - One clear next step"
    ],
    examples=[
        "High value: 'Get my exact script template that got 1M views'",
        "Low risk: 'Free, no email required, just comment HOOK'",
        "Alignment: 'If you're ready to grow, grab the full course'",
        "Urgency: 'Only available for the next 48 hours'",
        "Single action: 'Comment YES below (not just like)'"
    ]
)

# =============================================================================
# ALL FRAMEWORKS COLLECTION
# =============================================================================
ALL_FRAMEWORKS = [
    HOOK_MISTAKES,
    THREE_STEP_HOOK,
    SIX_STAGE_PSYCHOLOGY,
    FIVE_STORY_TECHNIQUES,
    VIDEO_STRUCTURE,
    SHORTS_FORMULA,
    RETENTION_TACTICS,
    CTA_FRAMEWORK
]

# =============================================================================
# HOOK TEMPLATES BY FRAMEWORK
# =============================================================================
HOOK_TEMPLATES = {
    "contrarian": [
        "Everyone says {common_belief}, but {contrarian_result}",
        "Stop doing {common_action}. Here's why it's killing your {outcome}",
        "{common_advice} sounds smart, except {negative_consequence}",
        "I tried {popular_method} for 30 days. The results were {unexpected}",
        "Why {expert_advice} is actually hurting your {goal}",
    ],
    "curiosity_gap": [
        "The real reason you're not {desired_outcome} (it's not what you think)",
        "I discovered {surprising_fact} and it changed everything",
        "What {successful_person} knows about {topic} that you don't",
        "The {topic} secret no one talks about",
        "Why your {current_approach} is secretly sabotaging you",
    ],
    "pain_agitation": [
        "Struggling with {pain_point}? You're making this 1 mistake",
        "If {pain_scenario} feels impossible, watch this",
        "The {pain_point} that cost me {loss} (and how to avoid it)",
        "I was {negative_state} until I discovered {solution}",
        "The #1 reason {target_audience} fail at {goal}",
    ],
    "social_proof": [
        "How I {achievement} in {timeframe} (step-by-step)",
        "This {strategy} got me {result} with only {effort}",
        "I analyzed {number} {things}. Here's what works",
        "From {bad_state} to {good_state}: My exact process",
        "The {system} that helped {number} people {achievement}",
    ],
    "how_to": [
        "How to {desired_outcome} in {timeframe} (even if {objection})",
        "The fastest way to {goal} without {common_problem}",
        "{number} {topic} hacks that actually work",
        "How I {action} and got {result} in {timeframe}",
        "The beginner's guide to {topic} (no fluff)",
    ]
}

# =============================================================================
# POWER WORDS AND PHRASES
# =============================================================================
POWER_WORDS = {
    "emotional": ["secret", "mistake", "truth", "shocking", "surprising", "devastating", "game-changing"],
    "urgency": ["now", "today", "immediately", "before it's too late", "don't wait"],
    "exclusivity": ["hidden", "unknown", "insider", "exclusive", "rarely shared"],
    "results": ["guaranteed", "proven", "tested", "verified", "backed by science"],
    "simplicity": ["easy", "simple", "fast", "quick", "step-by-step", "no fluff"],
    "authority": ["expert", "professional", "industry leader", "top", "best"]
}

CONTRAST_WORDS = ["but", "except", "however", "although", "yet", "despite", "while"]

# =============================================================================
# ANALYSIS PATTERNS
# =============================================================================
WEAK_PATTERNS = {
    "delay": [
        r"in this video",
        r"i want to talk about",
        r"today i'm going to",
        r"let me tell you",
        r"so basically",
    ],
    "confusion": [
        r"^this is",
        r"that thing",
        r"you know",
        r"kind of",
        r"sort of",
    ],
    "irrelevance": [
        r"my morning routine",
        r"what i ate",
        r"just wanted to share",
    ],
    "disinterest": [
        r"i think",
        r"maybe",
        r"possibly",
        r"i guess",
    ]
}

STRONG_PATTERNS = {
    "you_focused": [r"\byou\b", r"\byour\b"],
    "contrast": [r"\bbut\b", r"\bexcept\b", r"\bhowever\b", r"\byet\b"],
    "curiosity": [r"\bsecret\b", r"\bmistake\b", r"\bwhy\b", r"\bhow\b"],
    "specificity": [r"\$\d+", r"\d+%", r"\d+ days", r"\d+ steps"],
    "emotional": [r"\bshocking\b", r"\bsurprising\b", r"\bdevastating\b", r"\bgame.\w+\b"]
}


def get_random_template(category: str) -> str:
    """Get a random template from a category"""
    return random.choice(HOOK_TEMPLATES.get(category, []))


def get_framework_by_name(name: str) -> Optional[Framework]:
    """Get a framework by its name"""
    for fw in ALL_FRAMEWORKS:
        if fw.name.lower() == name.lower():
            return fw
    return None


def list_all_frameworks() -> List[str]:
    """Return list of all framework names"""
    return [fw.name for fw in ALL_FRAMEWORKS]
