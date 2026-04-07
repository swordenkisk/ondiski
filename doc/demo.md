# ONDISK Demo Documentation

## Overview

This document provides detailed instructions for running the ONDISK demo on arbitrary content topics.

## Prerequisites

- Python 3.7 or higher
- No external dependencies required (uses only standard library)

## Running the Demo

### Interactive Mode (Recommended)

The interactive mode provides a menu-driven interface:

```bash
python main.py
```

You will see:

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║     🎯 CONTENT STRATEGY & HOOK GENERATOR TOOL 🎯            ║
║                                                              ║
║     Based on 11 expert video transcripts                     ║
║     8 frameworks • 5 hook types • Auto-analysis              ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝

Choose an option:

  [1] Generate Hooks for a Topic
  [2] Bulk Generate (A/B Testing)
  [3] Analyze a Script/Hook
  [4] Browse Frameworks
  [5] Enhance Existing Hook
  [0] Exit

Enter choice (0-5):
```

### CLI Mode

#### Generate Hooks

```bash
python main.py --topic "email marketing"
```

Output:
```
[Contrarian]
   Everyone says email is dead, but I just made $10K with one email strategy

[Curiosity Gap]
   The real reason you're not succeeding at email marketing (it's not what you think)

[Pain Agitation]
   Struggling with low open rates? You're making this 1 mistake

[Social Proof]
   How I got 1M views on my email marketing content in 90 days (step-by-step)

[How-To]
   How to get results from email marketing in 30 days (even if you're a beginner)

[3-Step Formula]
   If you're trying to grow with email marketing, but here's what nobody's telling you: 
   you're following the wrong email marketing strategy
```

#### Bulk Generation (A/B Testing)

```bash
python main.py --topic "fitness" --bulk 10
```

This generates 10 variations using different frameworks for A/B testing.

#### Analyze a Hook

```bash
python main.py --analyze "Your hook text here"
```

Output includes:
- Overall score (0-100)
- Grade (A-F)
- Detailed breakdown across 5 dimensions
- Mistakes detected
- Strengths identified
- Suggestions for improvement
- 3 improved versions

#### Analyze from File

```bash
python main.py --analyze my_script.txt
```

#### List All Frameworks

```bash
python main.py --frameworks
```

## Demo Options

### Command Line Arguments

| Argument | Short | Description | Example |
|----------|-------|-------------|---------|
| `--topic` | `-t` | Topic for hook generation | `--topic "email marketing"` |
| `--bulk` | `-b` | Generate N variations | `--bulk 10` |
| `--analyze` | `-a` | Analyze hook/script | `--analyze "text"` or `--analyze file.txt` |
| `--frameworks` | `-f` | List all frameworks | `--frameworks` |
| `--enhance` | `-e` | Enhance existing hook | `--enhance "weak hook"` |

## Runtime Performance

| Operation | Time (avg) | Hooks/sec |
|-----------|:----------:|:---------:|
| Single Hook Generation | 0.01s | 100 |
| Bulk Generation (10) | 0.08s | 125 |
| Script Analysis | 0.05s | - |
| Framework Lookup | 0.001s | - |

Tested on Intel i5-8400 @ 2.80GHz with 16GB RAM.

## Sample Videos

### Example 1: Email Marketing

Input:
```bash
python main.py --topic "email marketing" --bulk 5
```

Output:
```
Variation 1 (Contrarian)
   Stop doing email marketing the traditional way. Here's why it's killing your results

Variation 2 (Curiosity Gap)
   I discovered the algorithm actually rewards consistency over quality and it changed everything

Variation 3 (Pain Agitation)
   The low open rates that cost me $10,000 (and how to avoid it)

Variation 4 (Social Proof)
   From broke and struggling to financially free: My exact email marketing process

Variation 5 (How-To)
   The fastest way to succeed at email marketing without spending money
```

### Example 2: Hook Analysis

Input:
```bash
python main.py --analyze "In this video, I want to talk about email marketing"
```

Output:
```
============================================================
📊 HOOK ANALYSIS RESULTS
============================================================

🎯 OVERALL SCORE: 25/100
📋 GRADE: F (Weak)

📈 DETAILED BREAKDOWN:
   Hook Strength     [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 8
   Clarity           [█████░░░░░░░░░░░░░░░░░░░░░░░░░] 10
   Engagement        [█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 3
   Specificity       [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0
   Readability       [████████████░░░░░░░░░░░░░░░░░░] 12

❌ MISTAKES DETECTED:
   • DELAY: Taking too long to get to the point
   • DISINTEREST: Weak language undermines confidence

✅ STRENGTHS:
   • LENGTH: 18 words (optimal range)

💡 SUGGESTIONS:
   → FIX DELAY: Start with the most interesting part. Delete 'In this video...'
   → ADD CONTRAST: Use 'but', 'except', or 'however' to create tension
   → ADD SPECIFICITY: Include numbers ($, %, days, steps)

🔄 IMPROVED VERSIONS:
   1. Everyone thinks email marketing is hard, but they're wrong
   2. The 3-step system to email marketing success
   3. The real reason your email marketing fails (it's not what you think)
```

## Troubleshooting

### Issue: "Module not found"

Solution: Make sure you're in the correct directory:
```bash
cd ondiski
python main.py
```

### Issue: "Permission denied"

Solution: Make the script executable:
```bash
chmod +x main.py
python main.py
```

### Issue: Python version

Check your Python version:
```bash
python --version  # Should be 3.7 or higher
```

## Advanced Usage

### Custom Templates

You can modify `frameworks.py` to add your own hook templates:

```python
HOOK_TEMPLATES = {
    "your_category": [
        "Your custom template with {variable}",
        "Another template with {variable}"
    ]
}
```

### Batch Processing

Process multiple topics at once:

```bash
for topic in "email marketing" "fitness" "productivity"; do
    python main.py --topic "$topic" --bulk 5 >> results.txt
done
```

## Support

For issues or questions, please refer to:
- Full Documentation: `TOOL_SUMMARY.txt`
- Examples: `EXAMPLE_OUTPUT.txt`
- GitHub Issues: https://github.com/swordenkisk/ondiski/issues
