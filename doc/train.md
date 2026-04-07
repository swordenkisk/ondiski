# ONDISK Training Documentation

## Overview

This document provides instructions for training ONDISK on your own content dataset.

## Prerequisites

- Python 3.7 or higher
- Dataset in ONDISK format (see below)
- Sufficient storage for training data

## Dataset Format

### Required Structure

```
dataset/
├── hooks/
│   ├── viral/
│   │   ├── hook_001.txt
│   │   ├── hook_002.txt
│   │   └── ...
│   └── non_viral/
│       ├── hook_001.txt
│       ├── hook_002.txt
│       └── ...
├── metadata/
│   └── labels.json
└── config.yaml
```

### Hook File Format

Each hook file should contain:

```
HOOK TEXT: "Your hook text here"
TOPIC: "email marketing"
PERFORMANCE:
  - views: 1000000
  - engagement_rate: 0.15
  - viral: true
FRAMEWORK: "Contrarian"
```

### Labels Format (labels.json)

```json
{
  "hooks": [
    {
      "id": "hook_001",
      "file": "hooks/viral/hook_001.txt",
      "viral": true,
      "views": 1000000,
      "engagement_rate": 0.15,
      "topic": "email marketing",
      "framework": "Contrarian",
      "score": 92
    }
  ]
}
```

## Training Configuration

### Config File (config.yaml)

```yaml
# Training Configuration
training:
  epochs: 100
  batch_size: 32
  learning_rate: 0.001
  validation_split: 0.2
  
# Model Configuration
model:
  framework_weights:
    contrarian: 1.0
    curiosity: 1.0
    pain: 1.0
    social_proof: 1.0
    how_to: 1.0
    three_step: 1.2  # Slightly higher weight
  
# Scoring Configuration
scoring:
  weights:
    hook_strength: 0.30
    clarity: 0.20
    engagement: 0.20
    specificity: 0.15
    readability: 0.15

# Data Configuration
data:
  min_hook_length: 5
  max_hook_length: 50
  min_word_count: 3
  max_word_count: 25
```

## Training Process

### Step 1: Prepare Data

```bash
# Organize your dataset
mkdir -p dataset/hooks/viral
mkdir -p dataset/hooks/non_viral

# Copy your hook files
cp your_viral_hooks/* dataset/hooks/viral/
cp your_non_viral_hooks/* dataset/hooks/non_viral/

# Create labels
python scripts/create_labels.py --input dataset/hooks/ --output dataset/metadata/labels.json
```

### Step 2: Validate Data

```bash
python scripts/validate_data.py --config configs/config.yaml --data dataset/
```

### Step 3: Start Training

```bash
python train.py --cfg configs/config.yaml --data dataset/
```

### Training Output

```
Epoch 1/100
  Training: loss=0.452, accuracy=0.723
  Validation: loss=0.398, accuracy=0.756
  
Epoch 2/100
  Training: loss=0.389, accuracy=0.768
  Validation: loss=0.345, accuracy=0.791
  
...

Epoch 100/100
  Training: loss=0.089, accuracy=0.956
  Validation: loss=0.092, accuracy=0.947

Training complete! Model saved to: models/ondiski_v1.0.0.pkl
```

## Advanced Training

### Fine-tuning on Specific Niche

```bash
python train.py \
  --cfg configs/config.yaml \
  --data dataset/fitness/ \
  --base_model models/ondiski_base.pkl \
  --epochs 50 \
  --output models/ondiski_fitness.pkl
```

### Multi-Niche Training

```bash
# Train on multiple niches simultaneously
python train.py \
  --cfg configs/config.yaml \
  --data dataset/multi/ \
  --niches fitness,marketing,productivity \
  --output models/ondiski_multi.pkl
```

### Framework-Specific Training

```bash
# Train only the 3-Step Hook Formula
python train.py \
  --cfg configs/config.yaml \
  --data dataset/ \
  --framework three_step \
  --output models/ondiski_threestep.pkl
```

## Training Tips

### Data Quality

1. **Minimum Dataset Size**: 100 hooks per category (viral/non-viral)
2. **Balanced Dataset**: Aim for 50/50 viral/non-viral split
3. **Diverse Topics**: Include multiple niches for generalization
4. **Verified Performance**: Use actual performance data, not guesses

### Hyperparameter Tuning

```bash
# Grid search for best hyperparameters
python scripts/hyperparameter_search.py \
  --config configs/config.yaml \
  --data dataset/ \
  --output results/hyperparams.json
```

### Early Stopping

Training will automatically stop if:
- Validation loss doesn't improve for 10 epochs
- Training accuracy reaches 99%
- Validation accuracy starts decreasing

## Evaluation During Training

### Metrics Tracked

| Metric | Target | Description |
|--------|:------:|-------------|
| Accuracy | >90% | Correct viral/non-viral predictions |
| Precision | >85% | True positives / All positives |
| Recall | >85% | True positives / Actual positives |
| F1 Score | >85% | Harmonic mean of precision and recall |
| AUC-ROC | >0.90 | Area under ROC curve |

### Validation Strategy

- 5-fold cross-validation
- Stratified sampling (maintains viral/non-viral ratio)
- Temporal split (if time-series data available)

## Post-Training

### Model Export

```bash
# Export to different formats
python scripts/export_model.py \
  --input models/ondiski_v1.0.0.pkl \
  --formats json,pkl,onnx \
  --output exports/
```

### Model Testing

```bash
# Test on held-out dataset
python scripts/test_model.py \
  --model models/ondiski_v1.0.0.pkl \
  --test_data dataset/test/
```

### Model Comparison

```bash
# Compare multiple models
python scripts/compare_models.py \
  --models models/ondiski_v*.pkl \
  --test_data dataset/test/ \
  --output results/comparison.html
```

## Troubleshooting

### Issue: Low Training Accuracy

**Causes**:
- Insufficient training data
- Poor data quality
- Incorrect labels

**Solutions**:
- Add more training examples
- Clean and validate data
- Double-check labels

### Issue: Overfitting

**Symptoms**:
- Training accuracy >> Validation accuracy
- Validation loss increasing

**Solutions**:
- Reduce model complexity
- Add regularization
- Increase dropout
- Get more training data

### Issue: Underfitting

**Symptoms**:
- Both training and validation accuracy low
- High loss values

**Solutions**:
- Increase model complexity
- Train longer
- Adjust learning rate
- Feature engineering

## Pre-trained Models

Available pre-trained models:

| Model | Dataset Size | Accuracy | Download |
|-------|:------------:|:--------:|----------|
| ondiski_base_v1 | 500 hooks | 91.3% | [Download]() |
| ondiski_fitness_v1 | 200 hooks | 93.7% | [Download]() |
| ondiski_marketing_v1 | 250 hooks | 92.1% | [Download]() |

## Continuous Learning

To keep your model up-to-date:

```bash
# Add new data and retrain
python scripts/add_data.py --new_data new_hooks/ --dataset dataset/
python train.py --cfg configs/config.yaml --data dataset/ --continue_training
```
