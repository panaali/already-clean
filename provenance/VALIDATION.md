# Migration verification (2026-10-20)

- All 851 preserved artifacts matched original source commits by byte count, SHA-256 and Git blob; independently checked by the coordinating agent.
- Both published follow-up subtrees were copied completely. Source removal covered 56 study-only paths after destination publication.
- Six retained ARC-only document extracts have separate current hashes and original historical hashes; the coordinator checked both bindings. No original review pins or saved numerical results were relabelled.
- All 44 destination Python files parsed successfully. Current destination documentation had zero broken relative links; source edits introduced zero new broken links against the tracked-tree baseline. Historical archived docs and raw agent packets are excluded from current doc-link checks.
- Original initial-study, T6, and T383 scoring scripts ran in disposable scratch storage; all three output summary files were byte-for-byte identical to the imported originals. No model was loaded and no activation or agent study was rerun.
- The first T6 scoring attempt stopped on an absent ignored pilot file. The archived pilot and original seed-0 neuron index draw were restored using the new preparation helper; one complete retry succeeded. Original scripts and outputs remain unchanged. The completed T6 retry took approximately 232.8 seconds wall time.

See [validation.json](validation.json) for hashes and scope. The original mechanical verdict and failed control gate remain preserved, including the distinction between inconclusive and supported findings. Old Git history and other source branches were not rewritten, and the external tutorial Artifact was not republished.
