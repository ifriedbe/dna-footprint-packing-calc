# DNA Footprint Packing Calculator

A small geometric feasibility calculator: given a set of required
functional positions (logic gates, relays, input/output elements) for
a DNA-origami-based nanostructure, checks whether they fit within a
target device footprint at a realistic addressable-pixel pitch.

Built while researching a candidate 8-bit adder design (DNA strand-
displacement logic + mechanical bump-pattern output) for a
nanotechnology project targeting the [Foresight Institute Feynman
Grand Prize](https://foresight.org/feynman-grand-prize/).

## What it does

Uses the independently-verified **6nm addressable-pixel resolution**
of DNA origami (from Rothemund's original DNA origami paper, *Nature*
2006 — each staple strand occupies a distinct, independently
addressable ~6nm position) as a real, citable minimum spacing, and
checks whether a given component count (logic gates + carry/signal
relays + input anchors + output elements) fits within a target
cube/grid size at that pitch.

## Usage

```bash
python3 footprint_packing_analysis.py
```

Edit the component-count constants at the top of the script
(`GATES_PER_FULL_ADDER`, `N_BITS`, etc.) to match your own design, or
import `main()` from another script.

## Background

This was the first check in a chain that found bundling/stiffness
requirements for a DNA nanostructure and its footprint requirements
trade off against each other in a non-obvious way: the geometrically
efficient design and the mechanically-adequate design turned out to be
the same one, once the underlying requirement was correctly specified
(a companion finding — see the [oxdna-bundle-toolkit](https://github.com/ifriedbe/oxdna-bundle-toolkit)
repo for the mechanical side of this analysis).

## Requirements

Python 3.9+, no external dependencies beyond the standard library.

## License

MIT — see `LICENSE`.
