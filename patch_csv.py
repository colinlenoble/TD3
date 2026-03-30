"""
Patches both td3_answers.ipynb and td3_questions.ipynb to load CSV files
directly with pd.read_csv() instead of using zipfile.
Also updates the Part-1 markdown explanation accordingly.
"""
import json

HIST_CSV  = "data/tasmintasmaxtasprtotprsn_France_CNRM-CERFACS-CNRM-CM5_historical_r1i1p1_CNRM-ALADIN63_v2_MF-ADAMONT-SAFRAN-1980-2011_day_19510101-20051231.csv"
RCP26_CSV = "data/tasmintasmaxtasprtotprsn_France_CNRM-CERFACS-CNRM-CM5_rcp26_r1i1p1_CNRM-ALADIN63_v2_MF-ADAMONT-SAFRAN-1980-2011_day_20060101-21001231.csv"
RCP45_CSV = "data/tasmintasmaxtasprtotprsn_France_CNRM-CERFACS-CNRM-CM5_rcp45_r1i1p1_CNRM-ALADIN63_v2_MF-ADAMONT-SAFRAN-1980-2011_day_20060101-21001231.csv"
RCP85_CSV = "data/tasmintasmaxtasprtotprsn_France_CNRM-CERFACS-CNRM-CM5_rcp85_r1i1p1_CNRM-ALADIN63_v2_MF-ADAMONT-SAFRAN-1980-2011_day_20060101-21001231.csv"

# ── new cell contents ──────────────────────────────────────────────────────

MD_PART1 = (
    "---\n"
    "## Part 1 - Loading the Data\n"
    "\n"
    "The data is stored as CSV files in the `data/` folder. Each file corresponds\n"
    "to one scenario and contains daily climate data for a point near Paris.\n"
    "\n"
    "We load them with `pd.read_csv()`, which we already know from TD2:\n"
    "\n"
    "```python\n"
    "df = pd.read_csv(\"data/my_file.csv\")\n"
    "```\n"
    "\n"
    "The columns are already named: `date`, `lat`, `lon`, `tasmin`, `tasmax`, `tas`, `prtot`, `prsn`.\n"
)

# answers versions (fully shown)
ANSWERS = {
    # 1.1  imports — no more zipfile needed
    "ae0ebc85c970": "import pandas as pd\n",

    # 1.2  load historical — simple pd.read_csv
    "607cbea4d040": (
        f"hist_csv = \"{HIST_CSV}\"\n"
        "\n"
        "df_hist = pd.read_csv(hist_csv)\n"
        "\n"
        "print(df_hist.head())\n"
        "print(df_hist.shape)\n"
    ),

    # 1.3  load RCPs
    "bdf738e8e1d2": (
        f"rcp26_csv = \"{RCP26_CSV}\"\n"
        f"rcp45_csv = \"{RCP45_CSV}\"\n"
        f"rcp85_csv = \"{RCP85_CSV}\"\n"
        "\n"
        "df_rcp26 = pd.read_csv(rcp26_csv)\n"
        "df_rcp45 = pd.read_csv(rcp45_csv)\n"
        "df_rcp85 = pd.read_csv(rcp85_csv)\n"
        "\n"
        "print(\"rcp26:\", df_rcp26.shape, \"| rcp45:\", df_rcp45.shape, \"| rcp85:\", df_rcp85.shape)\n"
    ),
}

# questions versions (scaffolded)
QUESTIONS = {
    # 1.1  imports — no more zipfile
    "ae0ebc85c970": "import pandas as pd\n",

    # 1.2  fully shown (worked example)
    "607cbea4d040": (
        f"hist_csv = \"{HIST_CSV}\"\n"
        "\n"
        "df_hist = pd.read_csv(hist_csv)\n"
        "\n"
        "print(df_hist.head())\n"
        "print(df_hist.shape)\n"
    ),

    # 1.3  paths given, pd.read_csv call to fill
    "bdf738e8e1d2": (
        f"rcp26_csv = \"{RCP26_CSV}\"\n"
        f"rcp45_csv = \"{RCP45_CSV}\"\n"
        f"rcp85_csv = \"{RCP85_CSV}\"\n"
        "\n"
        "df_rcp26 = pd.read_csv(rcp26_csv)\n"
        "df_rcp45 = ...\n"
        "df_rcp85 = ...\n"
        "\n"
        "print(\"rcp26:\", df_rcp26.shape, \"| rcp45:\", df_rcp45.shape, \"| rcp85:\", df_rcp85.shape)\n"
    ),
}

# Part-1 markdown cell id
MD_PART1_ID = "ba5b4ea638d8"

def patch(nb, cell_patches, md_patches):
    for cell in nb["cells"]:
        cid = cell["id"]
        if cell["cell_type"] == "code" and cid in cell_patches:
            cell["source"] = cell_patches[cid]
            cell["outputs"] = []
            cell["execution_count"] = None
        elif cell["cell_type"] == "markdown" and cid in md_patches:
            cell["source"] = md_patches[cid]

for fname, cell_patches in [
    ("td3_answers.ipynb",   ANSWERS),
    ("td3_questions.ipynb", QUESTIONS),
]:
    with open(fname, "r", encoding="utf-8") as f:
        nb = json.load(f)
    patch(nb, cell_patches, {MD_PART1_ID: MD_PART1})
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    print(f"patched {fname}")
