# already-clean

Independent verification of Goodfire's [“Neural Networks Are Already Clean”](https://already-clean.goodfire.com/), using Qwen3-0.6B, blinded explainer/judge studies, random-direction controls, and independent follow-up experiments.

The latest recorded result supports a scoped descriptive claim: about **65% of neuron poles versus 21% of dense random directions** were rated “one main job.” The independent gate-passing study measured a **44.6 percentage-point gap [36.3, 52.9]**. The texture-matched comparison remained inconclusive at the preregistered margin. This is one 0.6B model, a subjective rating protocol, and does not establish the essay's larger-model claims or full mechanistic understanding. See [INDEX](INDEX.md) for the authoritative inherited qualifications.

## Evidence

- [Initial preregistration](PREREGISTRATION.md), [results and review corrections](RESULTS.md), and [blinded packets, keys, and agent outputs](study/README.md).
- [T6 larger rerun](essay_h2_rerun/README.md): its control-validity gate failed, so its preregistered verdict remains inconclusive.
- [T383 independent check](essay_h2_check/README.md): gate-passing controls and a texture-matched neuron arm.
- [Independent review scripts](review/README.md).
- [Migration provenance and integrity manifest](provenance/README.md): original files, exact source commits, and SHA-256 hashes. Supplemental [AlgZoo evidence](algzoo/README.md) supplies context for the original combined report; ongoing ARC research lives in [clean-neurons](https://github.com/panaali/clean-neurons).

## Reproduce saved scoring

Run from the repository root. These commands use the committed packets and outputs; they do not load a language model or make agent calls. The scorers overwrite their summary JSON, so use a disposable checkout if preserving an exact file snapshot.

```sh
python -m venv .venv
. .venv/bin/activate
pip install numpy scipy
python tools/verify_manifest.py
python analyze.py
python tools/prepare_t6_replay.py
python essay_h2_rerun/analyze_t6.py essay_h2_rerun/keys
python essay_h2_check/score.py essay_h2_check/keys
```

Fresh activation collection additionally needs PyTorch, Transformers, PyArrow, the public Qwen checkpoint and pile-10k corpus; see `collect.py` and the experiment READMEs. The original ignored activation caches were not present in the inspected workspace, so they are not claimed to have migrated. Saved packets, answer keys, agent outputs and summary evidence are included.

The original preregistrations, deviations, failed gates, and frozen scores are preserved. This move does not rerun or strengthen any scientific claim.
