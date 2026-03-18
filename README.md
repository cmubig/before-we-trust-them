# AIFORD: Accuracy Isn't Enough

**Failure Analysis of Foundation Models in Robotic Decision Making**

<p align="center">
  <img src="static/images/overall-framework.png" width="90%" alt="AIFORD Evaluation Framework"/>
</p>

> Using large language models (LLMs) and vision-language models (VLMs) for robotic decision making raises a fundamental safety question: can these models remain reliable when spatial reasoning errors lead directly to unsafe actions?

## Overview

We evaluate current LLMs and VLMs on **seven diagnostic tasks** spanning three settings:

- **Complete Information** — Deterministic ASCII map navigation (Easy / Normal / Hard)
- **Incomplete Information** — Uncertain terrain maps + sequence-based reasoning
- **Safety-Oriented Spatial Reasoning (SOSR)** — Direction following + emergency escape scenarios

Our results reveal that strong average accuracy can obscure rare but **safety-critical failures**, motivating failure-focused evaluation before deploying foundation models in safety-critical robotic systems.

## Key Findings

| Finding | Detail |
|---|---|
| **32%** | Hard emergency prompts where Gemini-2.5 Flash prioritized document retrieval over evacuation |
| **0%** | Success rate for multiple models on map tasks as spatial complexity increased |
| **1%** | Runs where a hallucinated server-room route was suggested during fire evacuation |

- GPT-5 achieved 100% on complete map tasks but dropped to 93.3% on uncertain terrain
- Gemini-2.5 Flash scored only 67% on hard emergency escape, **underperforming** Gemini-2.0 Flash (100%)
- LLaMA-3-8b exhibited complete structural collapse across all map tasks (0%)

## Project Page

👉 [https://cmubig.github.io/AIFORD/](https://cmubig.github.io/AIFORD/)

## Repository Structure

```
AIFORD/
├── index.html                    # Project page
├── static/
│   ├── css/                      # Stylesheets
│   ├── js/                       # Scripts
│   └── images/                   # Figures
└── code/
    ├── ASCII Map/                # Map generation & LLM evaluation
    │   ├── generate_maps.py
    │   └── run_llm_map.py
    ├── SOSR/                     # Safety-Oriented Spatial Reasoning
    │   ├── gemini_direction_api_check.py
    │   ├── gemini_fire_prompt_single_run.py
    │   ├── openai_fire_prompt_batch_run.py
    │   └── llama.py
    └── Sequence/                 # Sequence-based reasoning
        ├── sequence_gemini.py
        ├── sequence_gpt.py
        ├── sequence_masking/     # 100 masking task images
        └── sequence_validation/  # 100 validation task images
```

## Authors

**Jua Han**\*¹, **Jaeyoon Seo**\*¹, **Jungbin Min**\*², **Sieun Choi**¹, **Huichan Seo**³, **Jihie Kim**¹, **Jean Oh**³

¹Dongguk University · ²Sungkyunkwan University · ³Carnegie Mellon University

\* Equal contribution

## Citation

```bibtex
@article{han2025accuracy,
  title={Accuracy Isn't Enough: Failure Analysis of Foundation Models in Robotic Decision Making},
  author={Han, Jua and Seo, Jaeyoon and Min, Jungbin and Choi, Sieun and Seo, Huichan and Kim, Jihie and Oh, Jean},
  year={2025},
  note={Under review}
}
```
