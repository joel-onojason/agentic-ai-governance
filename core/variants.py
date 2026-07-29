"""
core.variants
==============
The two configured variants of the shared maturity-model core.

Both variants use the same six dimensions and the same five levels. They
differ only in the weighting profile applied to the dimensions during
scoring. Public-sector weights raise D4 (human oversight) and D5 (data and
privacy) because NITDA 2020 and the GAID place the sharpest duty on those
dimensions in public institutions. Large-enterprise weights raise D1
(autonomy) and D2 (identity) because the CBN Risk-Based Cybersecurity
Framework 2024 places the sharpest duty on those dimensions in regulated
financial entities.

Reference: Table 3.3 in Chapter Three of the project thesis.
"""

from dataclasses import dataclass
from typing import Dict, Tuple


@dataclass(frozen=True)
class Variant:
    id: str
    name: str
    description: str
    weights: Dict[str, float]  # dimension id → weight; must sum to 1.00

    def validate(self) -> None:
        """Raise ValueError if weights do not sum to 1.00 within tolerance."""
        total = sum(self.weights.values())
        if abs(total - 1.0) > 1e-6:
            raise ValueError(
                f"Variant {self.id} weights sum to {total}, expected 1.00"
            )
        expected = {"D1", "D2", "D3", "D4", "D5", "D6"}
        if set(self.weights.keys()) != expected:
            raise ValueError(
                f"Variant {self.id} weights must cover exactly {expected}"
            )


PUBLIC_SECTOR = Variant(
    id="public_sector",
    name="Public Sector",
    description=(
        "For federal Ministries, Departments and Agencies, and federal "
        "regulatory and statutory bodies. Weights raise D4 (human oversight) "
        "and D5 (data and privacy) to reflect NITDA 2020 and GAID priorities."
    ),
    weights={
        "D1": 0.15,
        "D2": 0.15,
        "D3": 0.15,
        "D4": 0.20,
        "D5": 0.20,
        "D6": 0.15,
    },
)

LARGE_ENTERPRISE = Variant(
    id="large_enterprise",
    name="Large Enterprise",
    description=(
        "For deposit money banks, payment service banks, telecommunications "
        "operators, digital-services providers, and other commercial "
        "controllers registered as DCPMIs under NDPA s. 44. Weights raise D1 "
        "(autonomy) and D2 (identity) to reflect the CBN Risk-Based "
        "Cybersecurity Framework 2024 priorities."
    ),
    weights={
        "D1": 0.20,
        "D2": 0.20,
        "D3": 0.15,
        "D4": 0.15,
        "D5": 0.15,
        "D6": 0.15,
    },
)


ALL_VARIANTS: Tuple[Variant, ...] = (PUBLIC_SECTOR, LARGE_ENTERPRISE)


def get_variant(variant_id: str) -> Variant:
    for v in ALL_VARIANTS:
        if v.id == variant_id:
            return v
    raise KeyError(f"Unknown variant id: {variant_id}")
