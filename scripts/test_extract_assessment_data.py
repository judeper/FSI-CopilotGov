from __future__ import annotations

import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))

import extract_assessment_data  # noqa: E402


def test_parse_regulations_keeps_commas_inside_parenthetical_citations():
    reg_string = (
        "OCC Bulletin 2023-17, "
        "OCC Heightened Standards (12 CFR part 30, appendix D), "
        "FINRA Rule 3110"
    )
    assert extract_assessment_data.parse_regulations(reg_string) == [
        "OCC Bulletin 2023-17",
        "OCC Heightened Standards (12 CFR part 30, appendix D)",
        "FINRA Rule 3110",
    ]


def test_parse_regulations_preserves_normal_comma_separated_references():
    reg_string = "FINRA Rule 4511, FINRA Rule 3110, SEC Rule 17a-4"
    assert extract_assessment_data.parse_regulations(reg_string) == [
        "FINRA Rule 4511",
        "FINRA Rule 3110",
        "SEC Rule 17a-4",
    ]


def test_parse_regulations_keeps_12_cfr_part_and_appendix_together():
    reg_string = (
        "OCC Bulletin 2023-17, "
        "12 CFR part 30, appendix D (OCC Heightened Standards)"
    )
    assert extract_assessment_data.parse_regulations(reg_string) == [
        "OCC Bulletin 2023-17",
        "12 CFR part 30, appendix D (OCC Heightened Standards)",
    ]
