# Before We Trust Them

**Decision-Making Failures in Navigation of Foundation Models**

<p align="center">
  <img src="static/images/overall-framework.png" width="90%" alt="Evaluation Framework Overview"/>
</p>

> High success rates on navigation-related tasks do not necessarily translate into reliable decision making by foundation models.

## Overview

We evaluate current LLMs and VLMs on **six diagnostic tasks** spanning three settings:

- **Reasoning under Complete Spatial Information** — ASCII map navigation (Easy / Normal / Hard)
- **Reasoning under Incomplete Spatial Information** — Path planning with unknown cells + egocentric sequence reasoning
- **Reasoning under Safety-Relevant Information** — Orientation tracking + emergency evacuation scenarios

Our results show that important decision-making failures can persist even when overall performance is strong, underscoring the need for failure-focused analysis before foundation models can be trusted.

## Key Findings

| Finding | Detail |
|---|---|
| **93%** | GPT-5 on unknown-cell maps — yet the remaining 7% still included invalid paths |
| **67%** | Gemini-2.5 Flash on hard emergency evacuation, underperforming Gemini-2.0 Flash (100%) |
| **32%** | Hard emergency prompts where Gemini-2.5 Flash prioritized document retrieval over evacuation |

- GPT-5 achieved 100% on all complete map tasks but produced constraint violations on unknown-cell maps
- Newer models are not always safer — Gemini-2.5 Flash underperformed its predecessor on emergency evacuation
- Llama-3-8b exhibited complete structural collapse across all map tasks (0%)

## Project Page

👉 [https://cmubig.github.io/before-we-trust-them/](https://cmubig.github.io/before-we-trust-them/)

## Repository Structure

```
before-we-trust-them/
├── index.html                    # Project page
├── static/
│   ├── css/                      # Stylesheets
│   ├── js/                       # Scripts
│   └── images/                   # Figures
└── code/
    ├── ASCII Map/                # Map generation & LLM evaluation
    │   ├── generate_maps.py
    │   └── run_llm_map.py
    ├── SOSR/                     # Safety-relevant reasoning
    │   ├── gemini_direction_api_check.py
    │   ├── gemini_fire_prompt_single_run.py
    │   ├── openai_fire_prompt_batch_run.py
    │   └── llama.py
    └── Sequence/                 # Egocentric sequence reasoning
        ├── sequence_gemini.py
        ├── sequence_gpt.py
        ├── sequence_masking/     # 100 missing-frame selection images
        └── sequence_validation/  # 100 turn-direction inference images
```

## Authors

**Jua Han**\*¹, **Jaeyoon Seo**\*¹, **Jungbin Min**\*², **Sieun Choi**¹, **Huichan Seo**³, **Jihie Kim**¹, **Jean Oh**³

¹Dongguk University · ²Sungkyunkwan University · ³Carnegie Mellon University

\* Equal contribution

## Citation

```bibtex
@article{han2025beforewetrust,
  title={Before We Trust Them: Decision-Making Failures in Navigation of Foundation Models},
  author={Han, Jua and Seo, Jaeyoon and Min, Jungbin and Choi, Sieun and Seo, Huichan and Kim, Jihie and Oh, Jean},
  year={2025},
  url={https://cmubig.github.io/before-we-trust-them/}
}
```
