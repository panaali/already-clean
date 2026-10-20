# Migration provenance

The destination was empty before this import. `manifest.json` records the original source repository, immutable commits, original Git blob IDs, SHA-256 and byte counts for every preserved source artifact. The initial study comes from shared baseline `40f059fe09051164fdf04738b5b05e98c1271367`; T6 and T383 come from their separately published branch tips named in the manifest. Full original mixed-scope documents live under `source_snapshot/`; their relative links describe the old repository and are intentionally not rewritten.

Current destination entrypoint documents are new administrative guides. Original study scripts, packets, keys, outputs, and result snapshots are preserved byte-for-byte. Supplemental AlgZoo evidence is copied here for context and remains in the source repository.

Ignored activation/corpus/model caches were not present at the source checkout or the inspected workspace worktrees. They are not part of the tracked source evidence. Regenerate them with the retained collection scripts and public dependencies if needed. No credentials or environment files are imported.

The source cleanup applies to the current default branch. Old Git commits and other historical branches are not rewritten or deleted. This is a scientific-material migration, not a history purge.

Run `python tools/verify_manifest.py` to check preserved bytes. Archived historical documents are excluded from current documentation-link checks because they intentionally preserve the original context.
