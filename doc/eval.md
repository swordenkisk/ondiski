# ONDISK Evaluation Documentation

## Overview

This document describes how to evaluate ONDISK on your own content or reproduce the benchmark results.

## Quick Evaluation

### Evaluate a Single Hook

```bash
python main.py --analyze "Your hook text here"
```

### Evaluate from File

```bash
python main.py --analyze my_script.txt
```

### Batch Evaluation

```bash
python scripts/batch_evaluate.py --input hooks/ --output results.json
```

## Reproducing Benchmark Results

### Step 1: Download Benchmark Dataset

```bash
# Download the viral content dataset
wget https://github.com/swordenkisk/ondiski/releases/download/v1.0.0/benchmark_dataset.zip
unzip benchmark_dataset.zip -d dataset/
```

### Step 2: Run Evaluation

```bash
python eval.py \
  --dataset dataset/benchmark/ \
  --output results/benchmark_results.json
```

### Step 3: Generate Report

```bash
python scripts/generate_report.py \
  --results results/benchmark_results.json \
  --output results/report.html
```

## Evaluation Metrics

### Primary Metrics

#### 1. Hook Performance Score (HPS)

```python
from script_analyzer import ScriptAnalyzer

analyzer = ScriptAnalyzer()
result = analyzer.analyze("Your hook text")

print(f"HPS: {result.score}/100")
print(f"Grade: {result.grade}")
```

#### 2. Component Scores

| Component | Weight | Your Score |
|-----------|:------:|:----------:|
| Hook Strength | 30% | ? |
| Clarity | 20% | ? |
| Engagement | 20% | ? |
| Specificity | 15% | ? |
| Readability | 15% | ? |

### Secondary Metrics

#### 3. Mistake Detection

```bash
python scripts/detect_mistakes.py --input your_hook.txt
```

Detects:
- DELAY: Taking too long to get to the point
- CONFUSION: Unclear what the video is about
- IRRELEVANCE: Doesn't match viewer intent
- DISINTEREST: Fails to create curiosity gap

#### 4. Strength Identification

```bash
python scripts/identify_strengths.py --input your_hook.txt
```

Identifies:
- Audience focus (you/your usage)
- Contrast words (but/except/however)
- Specificity (numbers, $, %)
- Power words (secret, mistake, shocking)
- Curiosity gaps

## Framework-Specific Evaluation

### Evaluate with Specific Framework

```bash
# Use only the 3-Step Hook Formula
python eval.py \
  --dataset dataset/ \
  --framework three_step \
  --output results/threestep.json
```

### Compare Frameworks

```bash
python scripts/compare_frameworks.py \
  --dataset dataset/ \
  --frameworks all \
  --output results/framework_comparison.html
```

## Benchmark Datasets

### Available Datasets

| Dataset | Hooks | Viral Rate | Description |
|---------|:-----:|:----------:|-------------|
| benchmark_v1 | 500 | 45% | General content |
| youtube_v1 | 300 | 52% | YouTube-specific |
| tiktok_v1 | 400 | 58% | TikTok-specific |
| shorts_v1 | 250 | 61% | YouTube Shorts |

### Dataset Format

```json
{
  "dataset": "benchmark_v1",
  "hooks": [
    {
      "id": "hook_001",
      "text": "Stop sending emails...",
      "topic": "email marketing",
      "viral": true,
      "views": 1000000,
      "platform": "youtube",
      "actual_performance": {
        "views": 1000000,
        "likes": 50000,
        "comments": 3000,
        "shares": 2000
      }
    }
  ]
}
```

## Evaluation Results Format

### Output Structure

```json
{
  "evaluation_date": "2026-04-07",
  "dataset": "benchmark_v1",
  "total_hooks": 500,
  "summary": {
    "average_hps": 91.3,
    "median_hps": 92.1,
    "std_hps": 8.4,
    "grade_distribution": {
      "A": 342,
      "B": 112,
      "C": 35,
      "D": 8,
      "F": 3
    }
  },
  "hooks": [
    {
      "id": "hook_001",
      "text": "Stop sending emails...",
      "score": 92,
      "grade": "A",
      "mistakes": [],
      "strengths": ["Contrast", "Specificity"],
      "components": {
        "hook_strength": 28,
        "clarity": 19,
        "engagement": 18,
        "specificity": 14,
        "readability": 15
      }
    }
  ]
}
```

## Comparative Evaluation

### Compare with Baseline

```bash
python scripts/compare_with_baseline.py \
  --your_hooks your_hooks/ \
  --baseline baseline_hooks/ \
  --output results/comparison.html
```

### Compare with Competitors

```bash
python scripts/compare_methods.py \
  --methods ondiski,gpt4,template,random \
  --dataset dataset/ \
  --output results/method_comparison.html
```

## Statistical Analysis

### Significance Testing

```bash
python scripts/statistical_test.py \
  --results results/ondiski.json \
  --baseline results/baseline.json \
  --test ttest \
  --output results/statistics.txt
```

### Confidence Intervals

```bash
python scripts/confidence_intervals.py \
  --results results/ondiski.json \
  --confidence 0.95 \
  --output results/ci.json
```

## Visualization

### Generate Charts

```bash
# Score distribution
python scripts/visualize.py \
  --results results/ondiski.json \
  --chart distribution \
  --output charts/distribution.png

# Framework comparison
python scripts/visualize.py \
  --results results/ \
  --chart comparison \
  --output charts/comparison.png

# Grade distribution
python scripts/visualize.py \
  --results results/ondiski.json \
  --chart grades \
  --output charts/grades.png
```

## Custom Evaluation

### Define Custom Metrics

```python
# custom_metrics.py
from script_analyzer import ScriptAnalyzer

class CustomAnalyzer(ScriptAnalyzer):
    def custom_metric(self, text):
        # Your custom metric logic
        score = 0
        # ... calculate score
        return score

analyzer = CustomAnalyzer()
result = analyzer.analyze("Your hook")
```

### Run Custom Evaluation

```bash
python custom_eval.py \
  --dataset dataset/ \
  --metric custom \
  --output results/custom.json
```

## Continuous Evaluation

### Automated Testing

```bash
# Set up automated evaluation
python scripts/setup_ci.py --config .ondiskirc

# Run tests
pytest tests/
```

### Performance Monitoring

```bash
# Track performance over time
python scripts/track_performance.py \
  --history results/history/ \
  --output reports/trend.html
```

## Evaluation Checklist

- [ ] Dataset is properly formatted
- [ ] Labels are accurate
- [ ] Sufficient sample size (>100 hooks)
- [ ] Balanced classes (viral/non-viral)
- [ ] Multiple frameworks tested
- [ ] Statistical significance verified
- [ ] Results are reproducible
- [ ] Documentation is complete

## Troubleshooting

### Issue: Low Scores on Good Hooks

**Possible Causes**:
- Incorrect scoring weights
- Missing context
- Niche-specific differences

**Solutions**:
- Adjust scoring weights in config
- Provide topic context
- Use niche-specific models

### Issue: Inconsistent Results

**Possible Causes**:
- Random seed not set
- Different configurations
- Data quality issues

**Solutions**:
- Set random seed
- Use consistent config
- Clean and validate data

## Best Practices

1. **Use Multiple Datasets**: Test on diverse content
2. **Cross-Validate**: Use k-fold validation
3. **Statistical Testing**: Verify significance
4. **Document Everything**: Record all parameters
5. **Reproduce Results**: Share exact commands used
