# A Custom Model Trained Only on D&D Content

Goal: a language model whose D&D knowledge comes **only** from openly licensed
Dungeons & Dragons content — the corpus mapped by [README.md](README.md) —
usable as a rules oracle, DM assistant, and content generator.

## The honest constraint

The entire legal D&D corpus is small: the SRDs, open 5E systems, retroclones,
Wikipedia, and open datasets total on the order of **hundreds of MB of text**.
That is plenty to *teach* a model D&D. It is nowhere near enough to train a
capable language model *from scratch* (that takes trillions of tokens).
So "trained only on D&D content" means, in practice:

1. **Continued pretraining + fine-tuning** of an open-weights base model on
   D&D-only data — every gradient step after the base sees nothing but D&D.
2. Optionally, a small **from-scratch model** as a research artifact: it will
   speak fluent D&D and know the rules corpus, but it will not reason like a
   frontier model. Listed for completeness, not recommended as the main path.

## Corpus — license-filtered tiers

Every source carries a per-document license entry in `corpus/manifest.jsonl`
(source URL, license, retrieval date). No manifest entry, no training.

### Tier 1 — train freely (CC / ORC / public domain)

- SRD 5.2.1 and SRD 5.1 (CC-BY-4.0, Wizards of the Coast)
- Level Up A5E SRD (CC-BY-4.0), Black Flag Reference Document (ORC / CC-BY-4.0)
- Basic Fantasy RPG 4e (CC-BY-SA 4.0)
- Open5e open-licensed documents (per-document CC-BY-4.0)
- Wikipedia D&D articles (CC-BY-SA) — lore, history, settings overviews
- Public-domain art/text (Rackham etc.) for multimodal pairs, if vision is added

### Tier 2 — train with care (OGL 1.0a Open Game Content only)

- 13th Age SRD, OSE SRD, Swords & Wizardry, Labyrinth Lord — Open Game Content
  sections only; Product Identity stripped.
- 5e-bits / dnd5eapi datasets — SRD-derived data only.

### Excluded — never trained on

- Copyrighted D&D book text (any edition, any setting book) — even privately
  held copies. This is a standing rule, not a preference.
- 5etools data dumps (non-SRD book content).
- Forgotten Realms Wiki full text in the *public* model — it is CC-BY-SA, so it
  is legal, but it belongs to the separate private FR model (see below).

## Build plan

1. **Collect** — pull Tier 1 + Tier 2 sources from the README links into
   `corpus/raw/`, each with its manifest entry. Prefer structured sources
   (5e-srd-api JSON, Open5e API, Markdown SRDs) over PDF scraping.
2. **Clean** — dedupe (SRD 5.1 vs 5.2.1 overlap is large: keep both, tagged by
   edition), strip Product Identity from Tier 2, normalize stat blocks and
   spell formats to one schema, chunk by section.
3. **Instruction data** — generate from the structured data, not from another
   model's imagination: rules Q&A from SRD sections, stat-block completion,
   spell/monster lookups, encounter building from XP budgets, dice math.
   Every answer traceable to a corpus chunk.
4. **Train** — open base (Qwen / Llama / Mistral class, 7–14B), continued
   pretraining on the corpus, then LoRA or full fine-tune on the instruction
   set. Runs on one rented GPU or a local workstation; GCP billing status must
   be checked before any cloud run.
5. **Ground it** — ship the model with RAG over the same corpus (5e-srd-api /
   Open5e locally) so exact numbers come from retrieval, flavor from the model.
   Expose it as an MCP server (pattern: `procload/dnd-mcp`, `lorekeeper-mcp`)
   and as a neuron in the Ultron network.
6. **Evaluate** — fixed test set: 200 rules questions with SRD citations,
   stat-block validity checks (CR math, spell DCs), edition-confusion traps
   (5.1 vs 5.2.1), and refusal checks on non-SRD book content it must not know.

## The Forgotten Realms variant (private)

A second, private fine-tune adds the Realms corpus indexed by the companion
repo **awesome-forgotten-realms**: the FR Wiki (CC-BY-SA), Wikipedia's Realms
articles, and Dustin's private reference stores in Google Drive
(`fantasy-world-private`). Private because the corpus mix and the game material
around it are private — the model itself is never published with that data.

## Deliverables

- `corpus/manifest.jsonl` — every training source + license
- Dataset card + training config in this repo
- Weights hosted privately (Hugging Face private repo or local), served via
  Ollama / KoboldCpp
- Eval report against the test set above
