"""
Hook Generator Module
Generates hooks using multiple frameworks and templates
"""

import random
from typing import List, Dict, Optional
from frameworks import (
    HOOK_TEMPLATES, POWER_WORDS, CONTRAST_WORDS,
    get_random_template, THREE_STEP_HOOK
)


class HookGenerator:
    """Generate hooks using proven frameworks"""
    
    def __init__(self):
        self.templates = HOOK_TEMPLATES
        self.power_words = POWER_WORDS
        self.contrast_words = CONTRAST_WORDS
    
    def generate_contrarian_hook(self, topic: str, common_belief: str = "", 
                                  contrarian_result: str = "") -> Dict:
        """Generate a contrarian/opposite hook"""
        template = get_random_template("contrarian")
        
        # Auto-generate components if not provided
        if not common_belief:
            common_beliefs = {
                "email marketing": "email is dead",
                "social media": "you need to post every day",
                "fitness": "you need to work out 2 hours a day",
                "business": "you need money to start",
                "productivity": "you need to wake up at 5am",
                "content": "you need expensive equipment",
                "marketing": "you need a big budget",
                "learning": "you need natural talent"
            }
            common_belief = common_beliefs.get(topic.lower(), f"{topic} is hard")
        
        if not contrarian_result:
            contrarian_results = [
                f"I just made $10K with one {topic} strategy",
                f"I grew my {topic} by 300% doing the opposite",
                f"here's why that's completely wrong",
                f"I proved everyone wrong in 30 days"
            ]
            contrarian_result = random.choice(contrarian_results)
        
        hook = template.format(
            common_belief=common_belief,
            contrarian_result=contrarian_result,
            common_action=f"doing {topic} the traditional way",
            outcome="results",
            common_advice=f"The advice about {topic}",
            negative_consequence="it destroyed my progress",
            popular_method=topic,
            unexpected="shocking",
            expert_advice="what the gurus say",
            goal="growth"
        )
        
        return {
            "hook": hook,
            "framework": "Contrarian",
            "template": template,
            "components": {
                "common_belief": common_belief,
                "contrarian_result": contrarian_result
            }
        }
    
    def generate_curiosity_hook(self, topic: str, secret: str = "") -> Dict:
        """Generate a curiosity gap hook"""
        template = get_random_template("curiosity_gap")
        
        if not secret:
            secrets = [
                "the algorithm actually rewards consistency over quality",
                "timing matters more than content quality",
                "your niche is too broad",
                "you're posting at the wrong time",
                "engagement pods are hurting you"
            ]
            secret = random.choice(secrets)
        
        hook = template.format(
            desired_outcome=f"succeeding at {topic}",
            surprising_fact=secret,
            successful_person="top creators",
            topic=topic,
            current_approach="current strategy"
        )
        
        return {
            "hook": hook,
            "framework": "Curiosity Gap",
            "template": template,
            "components": {"secret": secret}
        }
    
    def generate_pain_hook(self, topic: str, pain_point: str = "") -> Dict:
        """Generate a pain-agitation hook"""
        template = get_random_template("pain_agitation")
        
        if not pain_point:
            pain_points = {
                "email marketing": "low open rates",
                "social media": "zero engagement",
                "fitness": "not seeing results",
                "business": "no sales",
                "productivity": "feeling overwhelmed",
                "content": "no views",
                "marketing": "wasting money on ads",
                "learning": "information overload"
            }
            pain_point = pain_points.get(topic.lower(), f"struggling with {topic}")
        
        hook = template.format(
            pain_point=pain_point,
            pain_scenario=f"getting results from {topic}",
            loss="$10,000",
            negative_state="ready to quit",
            solution=f"this one {topic} hack",
            target_audience="beginners",
            goal="success"
        )
        
        return {
            "hook": hook,
            "framework": "Pain Agitation",
            "template": template,
            "components": {"pain_point": pain_point}
        }
    
    def generate_social_proof_hook(self, topic: str, achievement: str = "") -> Dict:
        """Generate a social proof hook"""
        template = get_random_template("social_proof")
        
        if not achievement:
            achievements = [
                f"got 1M views on my {topic} content",
                f"built a 6-figure {topic} business",
                f"grew from 0 to 100K followers",
                f"generated $50K from {topic}"
            ]
            achievement = random.choice(achievements)
        
        hook = template.format(
            achievement=achievement,
            timeframe="90 days",
            strategy=topic,
            result="10x growth",
            effort="2 hours a day",
            number="100",
            things=f"{topic} accounts",
            bad_state="broke and struggling",
            good_state="financially free",
            system=f"{topic} framework"
        )
        
        return {
            "hook": hook,
            "framework": "Social Proof",
            "template": template,
            "components": {"achievement": achievement}
        }
    
    def generate_how_to_hook(self, topic: str, outcome: str = "") -> Dict:
        """Generate a how-to hook"""
        template = get_random_template("how_to")
        
        if not outcome:
            outcomes = [
                f"master {topic} faster",
                f"get results from {topic}",
                f"build a {topic} system",
                f"scale your {topic}"
            ]
            outcome = random.choice(outcomes)
        
        hook = template.format(
            desired_outcome=outcome,
            timeframe="30 days",
            objection="you're a beginner",
            goal=f"succeed at {topic}",
            common_problem="spending money",
            number="5",
            topic=topic,
            action="implemented this",
            result="3x growth"
        )
        
        return {
            "hook": hook,
            "framework": "How-To",
            "template": template,
            "components": {"outcome": outcome}
        }
    
    def generate_three_step_hook(self, topic: str) -> Dict:
        """Generate using Callaway's 3-Step Formula"""
        context_leans = [
            f"Everyone's talking about {topic} right now",
            f"If you're trying to grow with {topic}",
            f"You've probably heard that {topic} is the key"
        ]
        
        scroll_stops = [
            "but here's what nobody's telling you",
            "but I need to warn you about something",
            "but there's a massive problem"
        ]
        
        snapbacks = [
            f"the 'guru' advice about {topic} is actually hurting you",
            f"you're following the wrong {topic} strategy",
            f"this common {topic} mistake costs creators thousands"
        ]
        
        hook = f"{random.choice(context_leans)}, {random.choice(scroll_stops)}: {random.choice(snapbacks)}"
        
        return {
            "hook": hook,
            "framework": "3-Step Formula (Callaway)",
            "template": "Context Lean + Scroll Stop + Contrarian Snapback",
            "components": {
                "context_lean": context_leans,
                "scroll_stop": scroll_stops,
                "snapback": snapbacks
            }
        }
    
    def generate_bulk_hooks(self, topic: str, count: int = 5) -> List[Dict]:
        """Generate multiple hooks for A/B testing"""
        generators = [
            self.generate_contrarian_hook,
            self.generate_curiosity_hook,
            self.generate_pain_hook,
            self.generate_social_proof_hook,
            self.generate_how_to_hook,
            self.generate_three_step_hook
        ]
        
        hooks = []
        for i in range(count):
            generator = generators[i % len(generators)]
            hook_data = generator(topic)
            hook_data["variation"] = f"Variation {i + 1}"
            hooks.append(hook_data)
        
        return hooks
    
    def enhance_hook(self, hook: str, add_power_words: bool = True,
                     add_specificity: bool = True) -> str:
        """Enhance an existing hook with power words and specificity"""
        enhanced = hook
        
        if add_power_words:
            # Add emotional power words if missing
            emotional_words = self.power_words["emotional"]
            if not any(word in hook.lower() for word in emotional_words):
                enhanced = f"The {random.choice(emotional_words)} truth: {enhanced}"
        
        if add_specificity:
            # Add numbers if missing
            import re
            if not re.search(r'\d+', enhanced):
                enhanced = enhanced.replace("this", "this 3-step", 1)
        
        return enhanced


def demo():
    """Demo the hook generator"""
    gen = HookGenerator()
    topic = "email marketing"
    
    print(f"=== Hook Generation Demo: {topic} ===\n")
    
    print("1. CONTRARIAN HOOK:")
    result = gen.generate_contrarian_hook(topic)
    print(f"   {result['hook']}\n")
    
    print("2. CURIOSITY GAP HOOK:")
    result = gen.generate_curiosity_hook(topic)
    print(f"   {result['hook']}\n")
    
    print("3. PAIN AGITATION HOOK:")
    result = gen.generate_pain_hook(topic)
    print(f"   {result['hook']}\n")
    
    print("4. SOCIAL PROOF HOOK:")
    result = gen.generate_social_proof_hook(topic)
    print(f"   {result['hook']}\n")
    
    print("5. HOW-TO HOOK:")
    result = gen.generate_how_to_hook(topic)
    print(f"   {result['hook']}\n")
    
    print("6. 3-STEP FORMULA HOOK:")
    result = gen.generate_three_step_hook(topic)
    print(f"   {result['hook']}\n")
    
    print("=== BULK GENERATION (5 variations) ===\n")
    bulk = gen.generate_bulk_hooks(topic, 5)
    for h in bulk:
        print(f"{h['variation']} ({h['framework']}):")
        print(f"   {h['hook']}\n")


if __name__ == "__main__":
    demo()
