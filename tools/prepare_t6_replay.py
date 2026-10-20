"""Restore two small T6 scoring inputs without loading a model or collecting activations.

The index generator is exactly the seed/order/shape in collect_t6.py for Qwen3-0.6B.
The pilot is copied from the original committed post-unblinding archive.
Run from the repository root (or a disposable replay checkout).
"""
import shutil
from pathlib import Path
import numpy as np
out = Path('data/t6')
out.mkdir(parents=True, exist_ok=True)
pilot = out / 'pilot.json'
source = Path('essay_h2_rerun/keys/pilot_stats.json')
if pilot.exists():
    assert pilot.read_bytes() == source.read_bytes(), 'Refusing to overwrite a different pilot'
else:
    shutil.copyfile(source, pilot)
rng = np.random.default_rng(0)
indices = np.stack([rng.choice(3072, 32, replace=False) for _ in range(28)])
path = out / 'neuron_idx.npy'
if path.exists():
    assert np.array_equal(np.load(path), indices), 'Refusing to overwrite different indices'
else:
    np.save(path, indices)
print('Prepared archived pilot and deterministic neuron indices; no model calls.')
