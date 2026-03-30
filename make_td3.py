"""
Regenerates td3_questions.ipynb from td3_answers.ipynb.
- Copies all markdown cells unchanged.
- For each code cell, applies a scaffolded "questions" version that follows the
  Part-1.2/1.3 level of detail: structure fully shown, only the key value/
  expression replaced by `...`.
- Fixes the corrupted cell 20 in answers (traceback prefix) in the output.
"""
import json, copy, uuid

# ── scaffolded questions for each code cell (keyed by cell id) ────────────
# IDs from td3_answers.ipynb

QUESTIONS = {

    # 1.1  imports – fully shown (reference cell, nothing to fill)
    "ae0ebc85c970": (
        "# Import pandas and zipfile\n"
        "import pandas as pd\n"
        "import zipfile\n"
    ),

    # 1.2  load historical – fully shown (worked example, nothing to fill)
    "607cbea4d040": (
        "hist_zip = \"data/tasmintasmaxtasprtotprsn_France_CNRM-CERFACS-CNRM-CM5_historical_r1i1p1_CNRM-ALADIN63_v2_MF-ADAMONT-SAFRAN-1980-2011_day_19510101-20051231_2026000009198.zip\"\n"
        "\n"
        "col_names = [\"date\", \"lat\", \"lon\", \"tasmin\", \"tasmax\", \"tas\", \"prtot\", \"prsn\"]\n"
        "\n"
        "with zipfile.ZipFile(hist_zip) as z:\n"
        "    filename = z.namelist()[0]\n"
        "    with z.open(filename) as f:\n"
        "        df_hist = pd.read_csv(f, comment=\"#\", sep=r\"\\s+\", names=col_names)\n"
        "\n"
        "print(df_hist.head())\n"
        "print(df_hist.shape)\n"
    ),

    # 1.3  load RCPs – structure shown, only pd.read_csv(...) call to fill
    "bdf738e8e1d2": (
        "rcp26_zip = \"data/tasmintasmaxtasprtotprsn_France_CNRM-CERFACS-CNRM-CM5_rcp26_r1i1p1_CNRM-ALADIN63_v2_MF-ADAMONT-SAFRAN-1980-2011_day_20060101-21001231_2026000009199.zip\"\n"
        "rcp45_zip = \"data/tasmintasmaxtasprtotprsn_France_CNRM-CERFACS-CNRM-CM5_rcp45_r1i1p1_CNRM-ALADIN63_v2_MF-ADAMONT-SAFRAN-1980-2011_day_20060101-21001231_2026000009200.zip\"\n"
        "rcp85_zip = \"data/tasmintasmaxtasprtotprsn_France_CNRM-CERFACS-CNRM-CM5_rcp85_r1i1p1_CNRM-ALADIN63_v2_MF-ADAMONT-SAFRAN-1980-2011_day_20060101-21001231_2026000009201.zip\"\n"
        "\n"
        "# Load RCP 2.6\n"
        "with zipfile.ZipFile(rcp26_zip) as z:\n"
        "    with z.open(z.namelist()[0]) as f:\n"
        "        df_rcp26 = ...\n"
        "\n"
        "# Load RCP 4.5\n"
        "with zipfile.ZipFile(rcp45_zip) as z:\n"
        "    with z.open(z.namelist()[0]) as f:\n"
        "        df_rcp45 = ...\n"
        "\n"
        "# Load RCP 8.5\n"
        "with zipfile.ZipFile(rcp85_zip) as z:\n"
        "    with z.open(z.namelist()[0]) as f:\n"
        "        df_rcp85 = ...\n"
        "\n"
        "print(\"rcp26:\", df_rcp26.shape, \"| rcp45:\", df_rcp45.shape, \"| rcp85:\", df_rcp85.shape)\n"
    ),

    # 2.1  parse dates – function shown, only format string to fill
    "6169278678e5": (
        "for df in [df_hist, df_rcp26, df_rcp45, df_rcp85]:\n"
        "    df[\"date\"] = pd.to_datetime(df[\"date\"], format=...)\n"
        "\n"
        "print(df_hist[\"date\"].dtype)\n"
        "print(df_hist[\"date\"].head())\n"
    ),

    # 2.2  temperature – column names shown, only the offset value to fill
    "b8e0e8b3f48f": (
        "for df in [df_hist, df_rcp26, df_rcp45, df_rcp85]:\n"
        "    df[\"tasmin_c\"] = df[\"tasmin\"] - ...\n"
        "    df[\"tasmax_c\"] = df[\"tasmax\"] - ...\n"
        "    df[\"tas_c\"]    = df[\"tas\"]    - ...\n"
        "\n"
        "print(\"Historical mean temperature:\", df_hist[\"tas_c\"].mean().round(2), \"degC\")\n"
    ),

    # 2.3  precipitation – column shown, only the multiplier to fill
    "75ea68eb0b5d": (
        "for df in [df_hist, df_rcp26, df_rcp45, df_rcp85]:\n"
        "    df[\"precip_mm\"] = df[\"prtot\"] * ...\n"
        "\n"
        "print(\"Historical mean daily precipitation:\", df_hist[\"precip_mm\"].mean().round(2), \"mm/day\")\n"
    ),

    # 3.1  year – accessor chain shown up to the dot, method to fill
    "205bafd7fcb0": (
        "for df in [df_hist, df_rcp26, df_rcp45, df_rcp85]:\n"
        "    df[\"year\"] = df[\"date\"]....\n"
    ),

    # 3.2  annual means – first line fully shown, column name to fill for others
    "cddf1f8f16d7": (
        "annual_hist  = df_hist.groupby(\"year\")[\"tas_c\"].mean()\n"
        "annual_rcp26 = df_rcp26.groupby(\"year\")[...].mean()\n"
        "annual_rcp45 = df_rcp45.groupby(\"year\")[...].mean()\n"
        "annual_rcp85 = df_rcp85.groupby(\"year\")[...].mean()\n"
        "\n"
        "print(annual_hist.tail())\n"
    ),

    # 3.3  multi-scenario temperature plot – rcp26 fully shown, .values for others
    "18f54a6ab324": (
        "import matplotlib.pyplot as plt\n"
        "\n"
        "plt.figure(figsize=(12, 5))\n"
        "plt.plot(annual_hist.index,  annual_hist.values,  color=\"black\",  label=\"Historical\")\n"
        "plt.plot(annual_rcp26.index, annual_rcp26.values, color=\"blue\",   label=\"RCP 2.6\")\n"
        "plt.plot(annual_rcp45.index, ...,                  color=\"orange\", label=\"RCP 4.5\")\n"
        "plt.plot(annual_rcp85.index, ...,                  color=\"red\",    label=\"RCP 8.5\")\n"
        "plt.xlabel(\"Year\")\n"
        "plt.ylabel(\"Mean temperature (degC)\")\n"
        "plt.title(\"Annual mean temperature in Paris -- CNRM-CM5 / ALADIN63\")\n"
        "plt.legend()\n"
        "plt.show()\n"
    ),

    # 3.4  annual precipitation plot – rcp26 fully shown, .values for others
    "1cce2dae": (
        "annual_pr_hist  = df_hist.groupby(\"year\")[\"precip_mm\"].mean()\n"
        "annual_pr_rcp26 = df_rcp26.groupby(\"year\")[...].mean()\n"
        "annual_pr_rcp45 = df_rcp45.groupby(\"year\")[...].mean()\n"
        "annual_pr_rcp85 = df_rcp85.groupby(\"year\")[...].mean()\n"
        "\n"
        "plt.figure(figsize=(12, 5))\n"
        "plt.plot(annual_pr_hist.index,  annual_pr_hist.values,  color=\"black\",  label=\"Historical\")\n"
        "plt.plot(annual_pr_rcp26.index, ..., color=\"blue\",   label=\"RCP 2.6\")\n"
        "plt.plot(annual_pr_rcp45.index, ..., color=\"orange\", label=\"RCP 4.5\")\n"
        "plt.plot(annual_pr_rcp85.index, ..., color=\"red\",    label=\"RCP 8.5\")\n"
        "plt.xlabel(\"Year\")\n"
        "plt.ylabel(\"Precipitation (mm/day)\")\n"
        "plt.title(\"Annual mean precipitation in Paris -- CNRM-CM5 / ALADIN63\")\n"
        "plt.legend()\n"
        "plt.show()\n"
    ),

    # 3.5  rolling precipitation – window to fill, .values for rcp projections
    "4525253a": (
        "annual_pr_hist  = df_hist.groupby(\"year\")[\"precip_mm\"].mean().rolling(..., center=True).mean()\n"
        "annual_pr_rcp26 = df_rcp26.groupby(\"year\")[\"precip_mm\"].mean().rolling(..., center=True).mean()\n"
        "annual_pr_rcp45 = df_rcp45.groupby(\"year\")[\"precip_mm\"].mean().rolling(..., center=True).mean()\n"
        "annual_pr_rcp85 = df_rcp85.groupby(\"year\")[\"precip_mm\"].mean().rolling(..., center=True).mean()\n"
        "\n"
        "plt.figure(figsize=(12, 5))\n"
        "plt.plot(annual_pr_hist.index,  annual_pr_hist.values,  color=\"black\",  label=\"Historical\")\n"
        "plt.plot(annual_pr_rcp26.index, ..., color=\"blue\",   label=\"RCP 2.6\")\n"
        "plt.plot(annual_pr_rcp45.index, ..., color=\"orange\", label=\"RCP 4.5\")\n"
        "plt.plot(annual_pr_rcp85.index, ..., color=\"red\",    label=\"RCP 8.5\")\n"
        "plt.xlabel(\"Year\")\n"
        "plt.ylabel(\"Precipitation (mm/day)\")\n"
        "plt.legend()\n"
        "plt.show()\n"
    ),

    # 4.1  hot days historical – column shown, threshold to fill
    "1869e24566df": (
        "df_hist[\"hot_day\"] = df_hist[\"tasmax_c\"] > ...\n"
        "\n"
        "hot_days_hist = df_hist.groupby(\"year\")[\"hot_day\"].sum()\n"
        "\n"
        "print(\"Average hot days per year (historical):\", hot_days_hist.mean().round(1))\n"
    ),

    # 4.2  hot days scenarios – threshold + groupby column to fill, plot rcp26 shown
    "144e4bdf5b75": (
        "for df in [df_rcp26, df_rcp45, df_rcp85]:\n"
        "    df[\"hot_day\"] = df[\"tasmax_c\"] > ...\n"
        "\n"
        "hot_days_rcp26 = df_rcp26.groupby(\"year\")[\"hot_day\"].sum()\n"
        "hot_days_rcp45 = df_rcp45.groupby(\"year\")[...].sum()\n"
        "hot_days_rcp85 = df_rcp85.groupby(\"year\")[...].sum()\n"
        "\n"
        "plt.figure(figsize=(12, 5))\n"
        "plt.plot(hot_days_hist.index,  hot_days_hist.values,  color=\"black\",  label=\"Historical\")\n"
        "plt.plot(hot_days_rcp26.index, hot_days_rcp26.values, color=\"blue\",   label=\"RCP 2.6\")\n"
        "plt.plot(hot_days_rcp45.index, ...,                   color=\"orange\", label=\"RCP 4.5\")\n"
        "plt.plot(hot_days_rcp85.index, ...,                   color=\"red\",    label=\"RCP 8.5\")\n"
        "plt.xlabel(\"Year\")\n"
        "plt.ylabel(\"Number of hot days (tasmax > 30 degC)\")\n"
        "plt.title(\"Hot days per year in Paris\")\n"
        "plt.legend()\n"
        "plt.show()\n"
    ),

    # 4.3  warm nights – threshold + groupby column to fill, hist+rcp26 shown
    "72e86d254366": (
        "for df in [df_hist, df_rcp26, df_rcp45, df_rcp85]:\n"
        "    df[\"warm_night\"] = df[\"tasmin_c\"] > ...\n"
        "\n"
        "warm_hist  = df_hist.groupby(\"year\")[\"warm_night\"].sum()\n"
        "warm_rcp26 = df_rcp26.groupby(\"year\")[...].sum()\n"
        "warm_rcp45 = df_rcp45.groupby(\"year\")[...].sum()\n"
        "warm_rcp85 = df_rcp85.groupby(\"year\")[...].sum()\n"
        "\n"
        "plt.figure(figsize=(12, 5))\n"
        "plt.plot(warm_hist.index,  warm_hist.values,  color=\"black\",  label=\"Historical\")\n"
        "plt.plot(warm_rcp26.index, warm_rcp26.values, color=\"blue\",   label=\"RCP 2.6\")\n"
        "plt.plot(warm_rcp45.index, ...,               color=\"orange\", label=\"RCP 4.5\")\n"
        "plt.plot(warm_rcp85.index, ...,               color=\"red\",    label=\"RCP 8.5\")\n"
        "plt.xlabel(\"Year\")\n"
        "plt.ylabel(\"Number of warm nights (tasmin > 20 degC)\")\n"
        "plt.title(\"Warm nights per year in Paris\")\n"
        "plt.legend()\n"
        "plt.show()\n"
    ),

    # 5.1  reference period – upper bound year to fill, method call to fill
    "3f1c5fec1e78": (
        "df_ref = df_hist[(df_hist[\"year\"] >= 1981) & (df_hist[\"year\"] <= ...)]\n"
        "ref_mean_temp = df_ref[\"tas_c\"]....\n"
        "\n"
        "print(\"Reference mean temperature (1981-2010):\", ref_mean_temp.round(2), \"degC\")\n"
    ),

    # 5.2  future means – function given, rcp26 shown, rcp45/85 to fill
    "ae3916780ba6": (
        "def period_mean(df, start, end):\n"
        "    mask = (df[\"year\"] >= start) & (df[\"year\"] <= end)\n"
        "    return df[mask][\"tas_c\"].mean()\n"
        "\n"
        "near_future = {\n"
        "    \"RCP 2.6\": period_mean(df_rcp26, 2021, 2050),\n"
        "    \"RCP 4.5\": period_mean(df_rcp45, ..., ...),\n"
        "    \"RCP 8.5\": period_mean(df_rcp85, ..., ...),\n"
        "}\n"
        "\n"
        "far_future = {\n"
        "    \"RCP 2.6\": period_mean(df_rcp26, 2071, 2100),\n"
        "    \"RCP 4.5\": period_mean(df_rcp45, ..., ...),\n"
        "    \"RCP 8.5\": period_mean(df_rcp85, ..., ...),\n"
        "}\n"
        "\n"
        "print(\"Near future (2021-2050):\", {k: round(v, 2) for k, v in near_future.items()})\n"
        "print(\"Far future  (2071-2100):\", {k: round(v, 2) for k, v in far_future.items()})\n"
    ),

    # 5.3  delta T – near_future shown, far_future expression to fill
    "d83ae0ef760a": (
        "delta_near = {s: v - ref_mean_temp for s, v in near_future.items()}\n"
        "delta_far  = {s: v - ... for s, v in far_future.items()}\n"
        "\n"
        "print(\"Warming 2021-2050:\", {k: round(v, 2) for k, v in delta_near.items()})\n"
        "print(\"Warming 2071-2100:\", {k: round(v, 2) for k, v in delta_far.items()})\n"
    ),

    # 5.4  bar chart – delta_near shown, delta_far to fill
    "d24629d91174": (
        "import numpy as np\n"
        "\n"
        "scenarios = list(delta_near.keys())\n"
        "x = np.arange(len(scenarios))\n"
        "width = 0.35\n"
        "\n"
        "plt.figure(figsize=(8, 5))\n"
        "plt.bar(x - width/2, list(delta_near.values()), width, label=\"2021-2050\",\n"
        "        color=[\"lightblue\", \"lightyellow\", \"lightsalmon\"])\n"
        "plt.bar(x + width/2, list(delta_far...),        width, label=\"2071-2100\",\n"
        "        color=[\"blue\", \"orange\", \"red\"])\n"
        "plt.xticks(x, scenarios)\n"
        "plt.ylabel(\"Temperature change (degC) relative to 1981-2010\")\n"
        "plt.title(\"Projected warming in Paris by scenario\")\n"
        "plt.legend()\n"
        "plt.axhline(0, color=\"black\", linewidth=0.8)\n"
        "plt.show()\n"
    ),
}

# ── clean source of answers cell 20 (has a traceback prefix from a bad run) ─
CLEAN_ANSWERS = {
    "1cce2dae": (
        "annual_pr_hist  = df_hist.groupby(\"year\")[\"precip_mm\"].mean()\n"
        "annual_pr_rcp26 = df_rcp26.groupby(\"year\")[\"precip_mm\"].mean()\n"
        "annual_pr_rcp45 = df_rcp45.groupby(\"year\")[\"precip_mm\"].mean()\n"
        "annual_pr_rcp85 = df_rcp85.groupby(\"year\")[\"precip_mm\"].mean()\n"
        "\n"
        "plt.figure(figsize=(12, 5))\n"
        "plt.plot(annual_pr_hist.index,  annual_pr_hist.values,  color=\"black\",  label=\"Historical\")\n"
        "plt.plot(annual_pr_rcp26.index, annual_pr_rcp26.values, color=\"blue\",   label=\"RCP 2.6\")\n"
        "plt.plot(annual_pr_rcp45.index, annual_pr_rcp45.values, color=\"orange\", label=\"RCP 4.5\")\n"
        "plt.plot(annual_pr_rcp85.index, annual_pr_rcp85.values, color=\"red\",    label=\"RCP 8.5\")\n"
        "plt.xlabel(\"Year\")\n"
        "plt.ylabel(\"Precipitation (mm/day)\")\n"
        "plt.title(\"Annual mean precipitation in Paris -- CNRM-CM5 / ALADIN63\")\n"
        "plt.legend()\n"
        "plt.show()\n"
    ),
}

# ── load answers ────────────────────────────────────────────────────────────
with open("td3_answers.ipynb", "r", encoding="utf-8") as f:
    nb_answers = json.load(f)

# fix corrupted cell in answers
for cell in nb_answers["cells"]:
    if cell["cell_type"] == "code" and cell["id"] in CLEAN_ANSWERS:
        cell["source"] = CLEAN_ANSWERS[cell["id"]]
        cell["outputs"] = []
        cell["execution_count"] = None

with open("td3_answers.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb_answers, f, ensure_ascii=False, indent=1)
print("td3_answers.ipynb: fixed corrupted cell")

# ── build questions notebook ─────────────────────────────────────────────
nb_q = copy.deepcopy(nb_answers)
for cell in nb_q["cells"]:
    cell["outputs"] = []
    cell["execution_count"] = None
    if cell["cell_type"] == "code" and cell["id"] in QUESTIONS:
        cell["source"] = QUESTIONS[cell["id"]]

with open("td3_questions.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb_q, f, ensure_ascii=False, indent=1)

total_code = sum(1 for c in nb_q["cells"] if c["cell_type"] == "code")
scaffolded = sum(1 for c in nb_q["cells"] if c["cell_type"] == "code" and c["id"] in QUESTIONS)
print(f"td3_questions.ipynb: {scaffolded}/{total_code} code cells scaffolded")
