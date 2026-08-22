"""Geometric feasibility check for a DNA-origami logic-circuit footprint.

Question this was originally built to answer: can 8 full-adder logic
units (localized strand-displacement architecture) + a carry chain +
8-9 output elements be packed into a 50nm cube?

This is a combinatorial/packing calculation grounded in real, cited
DNA-origami numbers, not a molecular dynamics simulation -- MD tests
whether a *specific* structure is mechanically stable, not whether an
abstract component count fits a budget. This script is the packing
side; see the companion oxdna-bundle-toolkit repo for the mechanical
(stiffness/stability) side of the same design question.

Key real numbers used (all independently verified via literature
search):
  - 6 nm addressable "pixel" resolution on DNA origami: each staple
    strand position is an independently addressable anchor point,
    demonstrated in Rothemund's original DNA origami paper (Nature,
    2006), including using a raised-bump-vs-flat-staple encoding for
    binary information readable by AFM -- directly relevant precedent
    for the adder's bump-pattern output requirement, not just a
    resolution figure.
  - Standard Rothemund rectangle: ~100nm x 70nm, ~200+ staples
    (consistent with ~6nm pixel pitch over that area:
    100/6 ~= 16, 70/6 ~= 11, 16*11 ~= 176, same order as 200).
  - Localized DNA computing full adder (Chatterjee & Dalchau, Nature
    Nanotechnology 2017): built on a standard-size origami rectangle,
    exact hairpin spacing in nm not independently verified in this
    pass (source access blocked) -- 6nm pixel pitch used as the
    conservative, independently-sourced minimum spacing instead.
"""

PIXEL_NM = 6.0  # minimum addressable spacing between staple/hairpin anchor points

# Example component count for an 8-bit strand-displacement adder circuit
GATES_PER_FULL_ADDER = 3   # XOR, AND, OR (cSDR architecture, JACS 2022) per bit
N_BITS = 8
N_FULL_ADDERS = N_BITS
CARRY_RELAY_PER_JUNCTION = 1  # conservative: 1 relay hairpin between adjacent full-adders
                                # to bridge "double spacing" signal-decay limit noted
                                # in the localized-architecture paper
N_CARRY_JUNCTIONS = N_BITS - 1
N_OUTPUT_CANTILEVERS = N_BITS + 1  # 8 output bits + 1 internal (discarded) carry-out bit

def main():
    n_logic_gates = GATES_PER_FULL_ADDER * N_FULL_ADDERS
    n_carry_relays = CARRY_RELAY_PER_JUNCTION * N_CARRY_JUNCTIONS
    n_output = N_OUTPUT_CANTILEVERS
    n_input_reception = N_BITS * 2  # two 8-bit operands need distinct input anchor points

    total_positions = n_logic_gates + n_carry_relays + n_output + n_input_reception

    print("=== Component count (Concept C) ===")
    print(f"logic gates (3 per full-adder x {N_FULL_ADDERS} bits): {n_logic_gates}")
    print(f"carry-chain relay hairpins ({N_CARRY_JUNCTIONS} junctions): {n_carry_relays}")
    print(f"output cantilevers (8 bits + 1 discarded carry): {n_output}")
    print(f"input reception anchor points (2 x 8-bit operands): {n_input_reception}")
    print(f"TOTAL required addressable positions: {total_positions}")

    for cube_nm in (50.0, 70.0, 100.0):
        side_positions = int(cube_nm // PIXEL_NM)
        area_positions_2d = side_positions ** 2
        print(f"\n=== {cube_nm:.0f}nm budget (2D origami sheet, {PIXEL_NM}nm pixel pitch) ===")
        print(f"positions per side: {side_positions}  (floor({cube_nm:.0f}/{PIXEL_NM}))")
        print(f"total 2D grid slots available: {area_positions_2d}")
        margin = area_positions_2d - total_positions
        verdict = "FITS (by pixel count)" if margin >= 0 else "DOES NOT FIT"
        print(f"required: {total_positions}  available: {area_positions_2d}  margin: {margin:+d}  -> {verdict}")

    print("\n=== Caveats (read before trusting the verdict) ===")
    print("- This is a 2D pixel-count check only. It ignores: routing/wiring")
    print("  paths between non-adjacent gates, the physical size of the")
    print("  output cantilever mechanical elements (likely >1 pixel each,")
    print("  since they need to be free-standing/deflectable, not flat),")
    print("  the rigid-frame structural material needed for the arm-side")
    print("  stiffness requirement if a shared substrate is used, and")
    print("  reliable-operation spacing margins the localized-architecture")
    print("  paper may have used beyond the theoretical minimum pixel pitch.")
    print("- The exact hairpin spacing used in the actual published full-adder")
    print("  demonstration was not independently verified in this pass; 6nm")
    print("  is the conservative published minimum for ANY addressable DNA")
    print("  origami position, not confirmed as sufficient for two INTERACTING")
    print("  hairpin gates specifically (their real spacing could be larger).")


if __name__ == "__main__":
    main()
