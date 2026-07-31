"""
Kitchen Cabinet Ayurvedic Remedy Generator
A Streamlit app that suggests traditional Ayurvedic home remedies
using common kitchen spices and pantry ingredients.
"""

import streamlit as st

# ---------------------------------------------------------------------------
# Page config & styling
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Kitchen Cabinet Ayurvedic Remedy Generator",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #2d5a27;
        margin-bottom: 0.25rem;
    }
    .subtitle {
        color: #5a6b5a;
        font-size: 1.05rem;
        margin-bottom: 1.5rem;
    }
    .remedy-card {
        background: linear-gradient(135deg, #f7faf5 0%, #eef5ea 100%);
        border-left: 4px solid #4a7c3f;
        border-radius: 8px;
        padding: 1.25rem 1.5rem;
        margin-bottom: 1rem;
    }
    .disclaimer {
        background: #fff8e7;
        border: 1px solid #e6d5a8;
        border-radius: 8px;
        padding: 0.85rem 1.1rem;
        font-size: 0.9rem;
        color: #6b5a30;
    }
    .match-badge {
        display: inline-block;
        background: #4a7c3f;
        color: white;
        border-radius: 4px;
        padding: 0.15rem 0.55rem;
        font-size: 0.8rem;
        margin-right: 0.35rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Knowledge base: kitchen-cabinet Ayurvedic remedies
# ---------------------------------------------------------------------------
INGREDIENTS = [
    "Turmeric (Haldi)",
    "Ginger (Adrak)",
    "Cumin (Jeera)",
    "Coriander (Dhania)",
    "Fennel (Saunf)",
    "Fenugreek (Methi)",
    "Black Pepper (Kali Mirch)",
    "Cinnamon (Dalchini)",
    "Cardamom (Elaichi)",
    "Clove (Laung)",
    "Ajwain (Carom Seeds)",
    "Mustard Seeds (Rai)",
    "Holy Basil / Tulsi",
    "Honey",
    "Ghee",
    "Lemon",
    "Garlic",
    "Onion",
    "Yogurt / Curd",
    "Milk",
    "Coconut Oil",
    "Rock Salt (Sendha Namak)",
    "Jaggery (Gur)",
    "Mint (Pudina)",
    "Asafoetida (Hing)",
]

AILMENTS = [
    "Cold & Cough",
    "Sore Throat",
    "Indigestion / Acidity",
    "Bloating & Gas",
    "Nausea",
    "Headache",
    "Joint Pain / Inflammation",
    "Poor Immunity",
    "Insomnia / Restlessness",
    "Skin Irritation",
    "Constipation",
    "Low Energy / Fatigue",
    "Seasonal Allergies",
    "Stress & Anxiety",
]

DOSHAS = ["Vata", "Pitta", "Kapha", "Not sure / Tridoshic"]

# Each remedy: title, ailments, doshas helped, required ingredients (subset),
# optional ingredients, method, benefits, precautions
REMEDIES = [
    {
        "title": "Golden Turmeric Milk (Haldi Doodh)",
        "ailments": ["Poor Immunity", "Joint Pain / Inflammation", "Cold & Cough", "Low Energy / Fatigue"],
        "doshas": ["Vata", "Kapha", "Not sure / Tridoshic"],
        "required": ["Turmeric (Haldi)", "Milk"],
        "helpful": ["Black Pepper (Kali Mirch)", "Ghee", "Honey", "Cinnamon (Dalchini)", "Ginger (Adrak)"],
        "method": (
            "1. Warm 1 cup of milk gently (do not boil hard).\n"
            "2. Whisk in ½ tsp turmeric and a pinch of black pepper.\n"
            "3. Optional: add a drop of ghee, a pinch of cinnamon, or fresh ginger.\n"
            "4. Sweeten lightly with honey after removing from heat.\n"
            "5. Sip warm, preferably in the evening."
        ),
        "benefits": "Supports immunity, eases mild inflammation, and soothes the respiratory tract.",
        "precautions": "Avoid excess turmeric if you have gallstones or take blood thinners. Honey should not be heated.",
    },
    {
        "title": "Fresh Ginger Tea (Adrak Chai)",
        "ailments": ["Cold & Cough", "Nausea", "Indigestion / Acidity", "Bloating & Gas", "Low Energy / Fatigue"],
        "doshas": ["Vata", "Kapha", "Not sure / Tridoshic"],
        "required": ["Ginger (Adrak)"],
        "helpful": ["Honey", "Lemon", "Black Pepper (Kali Mirch)", "Tulsi", "Holy Basil / Tulsi", "Cinnamon (Dalchini)"],
        "method": (
            "1. Crush or slice 1-inch fresh ginger.\n"
            "2. Boil in 1½ cups water for 5–8 minutes.\n"
            "3. Add a squeeze of lemon and/or a pinch of black pepper if available.\n"
            "4. Strain; cool slightly and stir in honey if desired.\n"
            "5. Drink warm, 1–2 times daily."
        ),
        "benefits": "Kindles digestive fire (agni), clears mild congestion, and settles nausea.",
        "precautions": "Use sparingly if you have high Pitta (excess heat, acidity, or ulcers).",
    },
    {
        "title": "Cumin-Coriander-Fennel Digestive Tea (CCF Tea)",
        "ailments": ["Indigestion / Acidity", "Bloating & Gas", "Constipation", "Stress & Anxiety"],
        "doshas": ["Vata", "Pitta", "Kapha", "Not sure / Tridoshic"],
        "required": ["Cumin (Jeera)", "Coriander (Dhania)", "Fennel (Saunf)"],
        "helpful": ["Ginger (Adrak)", "Mint (Pudina)"],
        "method": (
            "1. Mix equal parts cumin, coriander, and fennel seeds (½ tsp each).\n"
            "2. Steep in 2 cups hot water for 5–10 minutes (or lightly simmer).\n"
            "3. Strain and sip warm between meals.\n"
            "4. Optional: add a few mint leaves for a cooling finish."
        ),
        "benefits": "A classic tridoshic brew that supports digestion and gentle detox.",
        "precautions": "Generally safe; reduce if stools become too loose.",
    },
    {
        "title": "Ajwain Digestive Water",
        "ailments": ["Bloating & Gas", "Indigestion / Acidity", "Nausea"],
        "doshas": ["Vata", "Kapha", "Not sure / Tridoshic"],
        "required": ["Ajwain (Carom Seeds)"],
        "helpful": ["Rock Salt (Sendha Namak)", "Lemon", "Ginger (Adrak)", "Asafoetida (Hing)"],
        "method": (
            "1. Crush ½ tsp ajwain lightly.\n"
            "2. Steep in 1 cup hot water for 5 minutes.\n"
            "3. Add a pinch of rock salt and a few drops of lemon if desired.\n"
            "4. Strain and sip slowly after meals."
        ),
        "benefits": "Relieves gas, bloating, and heaviness after eating.",
        "precautions": "Heating; avoid large amounts in high Pitta or pregnancy without guidance.",
    },
    {
        "title": "Tulsi–Honey Throat Soother",
        "ailments": ["Sore Throat", "Cold & Cough", "Seasonal Allergies"],
        "doshas": ["Vata", "Kapha", "Not sure / Tridoshic"],
        "required": ["Holy Basil / Tulsi", "Honey"],
        "helpful": ["Ginger (Adrak)", "Black Pepper (Kali Mirch)", "Turmeric (Haldi)", "Lemon"],
        "method": (
            "1. Boil 8–10 tulsi leaves in 1 cup water for 5 minutes.\n"
            "2. Optional: add a slice of ginger or a pinch of turmeric.\n"
            "3. Strain, cool until warm (not hot), then mix in 1 tsp honey.\n"
            "4. Sip slowly; can be taken 2–3 times a day."
        ),
        "benefits": "Soothes the throat, supports respiratory comfort, and eases mild coughs.",
        "precautions": "Do not give honey to children under 1 year. Do not boil honey.",
    },
    {
        "title": "Honey–Black Pepper–Ginger Cough Paste",
        "ailments": ["Cold & Cough", "Sore Throat"],
        "doshas": ["Vata", "Kapha", "Not sure / Tridoshic"],
        "required": ["Honey", "Black Pepper (Kali Mirch)", "Ginger (Adrak)"],
        "helpful": ["Turmeric (Haldi)", "Clove (Laung)"],
        "method": (
            "1. Mix 1 tsp honey with a pinch of freshly crushed black pepper.\n"
            "2. Add a few drops of ginger juice (or finely grated ginger).\n"
            "3. Optional: pinch of turmeric or one crushed clove.\n"
            "4. Take ½–1 tsp as needed for cough (up to 2–3 times daily)."
        ),
        "benefits": "Traditional Kapha-pacifying mix for productive cough and throat irritation.",
        "precautions": "Not for infants. Limit if Pitta is aggravated (burning throat, acidity).",
    },
    {
        "title": "Warm Lemon–Honey Water",
        "ailments": ["Constipation", "Poor Immunity", "Low Energy / Fatigue", "Indigestion / Acidity"],
        "doshas": ["Vata", "Kapha", "Not sure / Tridoshic"],
        "required": ["Lemon", "Honey"],
        "helpful": ["Ginger (Adrak)", "Rock Salt (Sendha Namak)"],
        "method": (
            "1. Squeeze half a lemon into a glass of warm (not boiling) water.\n"
            "2. Stir in 1 tsp honey.\n"
            "3. Optional: a thin slice of ginger or a tiny pinch of rock salt.\n"
            "4. Drink first thing in the morning on an empty stomach."
        ),
        "benefits": "Gently awakens digestion, supports hydration, and encourages regularity.",
        "precautions": "May aggravate acidity in high Pitta; take after food if sensitive.",
    },
    {
        "title": "Fenugreek Soaking Water",
        "ailments": ["Indigestion / Acidity", "Low Energy / Fatigue", "Constipation", "Joint Pain / Inflammation"],
        "doshas": ["Vata", "Kapha", "Not sure / Tridoshic"],
        "required": ["Fenugreek (Methi)"],
        "helpful": ["Honey", "Lemon"],
        "method": (
            "1. Soak 1 tsp fenugreek seeds in a cup of water overnight.\n"
            "2. In the morning, strain and drink the water.\n"
            "3. Chew the softened seeds if comfortable, or discard.\n"
            "4. Optional: add a few drops of lemon."
        ),
        "benefits": "Supports metabolic balance, digestion, and mild joint comfort.",
        "precautions": "May lower blood sugar; monitor if on diabetes medication. Avoid excess in pregnancy.",
    },
    {
        "title": "Cinnamon–Cardamom Comfort Brew",
        "ailments": ["Cold & Cough", "Indigestion / Acidity", "Stress & Anxiety", "Insomnia / Restlessness"],
        "doshas": ["Vata", "Kapha", "Not sure / Tridoshic"],
        "required": ["Cinnamon (Dalchini)", "Cardamom (Elaichi)"],
        "helpful": ["Milk", "Honey", "Ginger (Adrak)", "Clove (Laung)"],
        "method": (
            "1. Simmer a small cinnamon stick and 2 crushed cardamom pods in 1½ cups water (or milk) for 5–7 minutes.\n"
            "2. Optional: add a thin ginger slice or one clove.\n"
            "3. Strain; sweeten with honey after cooling slightly.\n"
            "4. Enjoy warm in the evening for calm and comfort."
        ),
        "benefits": "Warming, aromatic brew that settles digestion and eases evening restlessness.",
        "precautions": "Cinnamon is heating; use modest amounts if Pitta is high.",
    },
    {
        "title": "Cooling Coriander–Mint Infusion",
        "ailments": ["Indigestion / Acidity", "Skin Irritation", "Stress & Anxiety", "Headache"],
        "doshas": ["Pitta", "Not sure / Tridoshic"],
        "required": ["Coriander (Dhania)", "Mint (Pudina)"],
        "helpful": ["Fennel (Saunf)", "Lemon", "Honey"],
        "method": (
            "1. Lightly crush 1 tsp coriander seeds; add a small handful of mint leaves.\n"
            "2. Pour 1½ cups hot water over them and steep 8–10 minutes.\n"
            "3. Strain; cool to room temperature or lightly chill.\n"
            "4. Optional: squeeze of lemon and a touch of honey."
        ),
        "benefits": "Cooling Pitta-pacifying drink for heat, irritability, and mild acidity.",
        "precautions": "Prefer warm (not iced) drinks if Vata is high or digestion is weak.",
    },
    {
        "title": "Garlic–Ghee Joint Comfort",
        "ailments": ["Joint Pain / Inflammation", "Low Energy / Fatigue"],
        "doshas": ["Vata", "Kapha", "Not sure / Tridoshic"],
        "required": ["Garlic", "Ghee"],
        "helpful": ["Turmeric (Haldi)", "Black Pepper (Kali Mirch)", "Ginger (Adrak)"],
        "method": (
            "1. Gently warm 1 tsp ghee; add 1–2 crushed garlic cloves.\n"
            "2. Sauté on low heat until fragrant (do not burn).\n"
            "3. Optional: pinch of turmeric and black pepper.\n"
            "4. Take with warm rice or bread, or as directed by a practitioner.\n"
            "5. For external ease: warm ghee alone may be massaged onto stiff joints."
        ),
        "benefits": "Traditional Vata-soothing preparation supporting circulation and joint comfort.",
        "precautions": "Garlic is heating and pungent; reduce if Pitta or acidity is high.",
    },
    {
        "title": "Yogurt–Cumin Cooling Raita Base",
        "ailments": ["Indigestion / Acidity", "Bloating & Gas", "Stress & Anxiety"],
        "doshas": ["Pitta", "Vata", "Not sure / Tridoshic"],
        "required": ["Yogurt / Curd", "Cumin (Jeera)"],
        "helpful": ["Mint (Pudina)", "Rock Salt (Sendha Namak)", "Coriander (Dhania)", "Asafoetida (Hing)"],
        "method": (
            "1. Whisk ½ cup fresh yogurt with a little water until smooth.\n"
            "2. Roast and crush ½ tsp cumin; stir in with a pinch of rock salt.\n"
            "3. Add chopped mint or coriander if available.\n"
            "4. Eat at lunch (prefer room temperature, not ice-cold)."
        ),
        "benefits": "Supports digestion and cools mild Pitta when taken appropriately.",
        "precautions": "Avoid heavy yogurt at night or if Kapha is congested; prefer fresh, not sour curd.",
    },
    {
        "title": "Clove–Honey Tooth & Throat Ease",
        "ailments": ["Sore Throat", "Headache", "Cold & Cough"],
        "doshas": ["Vata", "Kapha", "Not sure / Tridoshic"],
        "required": ["Clove (Laung)", "Honey"],
        "helpful": ["Ginger (Adrak)", "Black Pepper (Kali Mirch)"],
        "method": (
            "1. Crush 1 clove finely.\n"
            "2. Mix with ½ tsp honey.\n"
            "3. Hold briefly in the mouth, then swallow slowly.\n"
            "4. For mild headache: gently inhale the aroma of warm clove tea (do not apply oil undiluted near eyes)."
        ),
        "benefits": "Classic kitchen remedy for throat discomfort and oral ease.",
        "precautions": "Clove is strong; use sparingly. Avoid undiluted clove oil on gums without guidance.",
    },
    {
        "title": "Mustard–Turmeric Warm Compress Support",
        "ailments": ["Joint Pain / Inflammation", "Cold & Cough"],
        "doshas": ["Vata", "Kapha", "Not sure / Tridoshic"],
        "required": ["Mustard Seeds (Rai)", "Turmeric (Haldi)"],
        "helpful": ["Coconut Oil", "Ghee"],
        "method": (
            "1. Warm 1–2 tsp coconut oil or ghee with a pinch of turmeric (external use).\n"
            "2. For chest comfort during cold: a mild mustard plaster tradition exists—"
            "use only with proper dilution and short contact; discontinue if skin burns.\n"
            "3. Prefer simple warm oil massage with turmeric for joint stiffness when unsure.\n"
            "4. Pair with warm ginger tea internally."
        ),
        "benefits": "Warming external support for Kapha-Vata stiffness and chill.",
        "precautions": "Mustard can irritate skin. Patch-test; never use on broken skin or for children without advice.",
    },
    {
        "title": "Jaggery–Ginger Digestive Bite",
        "ailments": ["Indigestion / Acidity", "Constipation", "Low Energy / Fatigue", "Cold & Cough"],
        "doshas": ["Vata", "Kapha", "Not sure / Tridoshic"],
        "required": ["Jaggery (Gur)", "Ginger (Adrak)"],
        "helpful": ["Ajwain (Carom Seeds)", "Fennel (Saunf)", "Black Pepper (Kali Mirch)"],
        "method": (
            "1. Mix a small piece of jaggery with a pinch of grated ginger.\n"
            "2. Optional: tiny pinch of ajwain or fennel.\n"
            "3. Take after meals as a digestive morsel.\n"
            "4. Or dissolve in warm water as a simple evening drink."
        ),
        "benefits": "Supports digestion, mild energy, and Kapha-clearing warmth.",
        "precautions": "Limit if blood sugar is a concern or Pitta/acidity is high.",
    },
    {
        "title": "Warm Ghee & Warm Milk for Rest",
        "ailments": ["Insomnia / Restlessness", "Stress & Anxiety", "Constipation", "Low Energy / Fatigue"],
        "doshas": ["Vata", "Not sure / Tridoshic"],
        "required": ["Ghee", "Milk"],
        "helpful": ["Cardamom (Elaichi)", "Nutmeg (if available)", "Honey", "Turmeric (Haldi)"],
        "method": (
            "1. Warm 1 cup milk; stir in ½–1 tsp ghee.\n"
            "2. Optional: crushed cardamom for aroma.\n"
            "3. Drink 30–45 minutes before bed.\n"
            "4. Combine with a calm evening routine (dim lights, light stretching)."
        ),
        "benefits": "Classic Vata-nourishing night drink to support sleep and grounding.",
        "precautions": "Heavy for Kapha; skip if congested or dairy-intolerant. Use plant milk alternatives as needed.",
    },
    {
        "title": "Asafoetida (Hing) Gas-Relief Tempering",
        "ailments": ["Bloating & Gas", "Indigestion / Acidity"],
        "doshas": ["Vata", "Kapha", "Not sure / Tridoshic"],
        "required": ["Asafoetida (Hing)", "Ghee"],
        "helpful": ["Cumin (Jeera)", "Ajwain (Carom Seeds)", "Ginger (Adrak)", "Rock Salt (Sendha Namak)"],
        "method": (
            "1. Heat ½ tsp ghee; add a tiny pinch of hing (a little goes a long way).\n"
            "2. Optional: cumin or ajwain seeds.\n"
            "3. Pour over warm lentils, vegetables, or mix into warm water with a pinch of salt.\n"
            "4. Use in cooking regularly for digestive support."
        ),
        "benefits": "Traditional anti-flatulent tempering that calms Vata in the gut.",
        "precautions": "Very pungent; use minute amounts. Avoid if sensitive to sulfurous spices.",
    },
    {
        "title": "Onion–Honey Syrup (Traditional Cold Support)",
        "ailments": ["Cold & Cough", "Sore Throat"],
        "doshas": ["Kapha", "Vata", "Not sure / Tridoshic"],
        "required": ["Onion", "Honey"],
        "helpful": ["Ginger (Adrak)", "Black Pepper (Kali Mirch)", "Lemon"],
        "method": (
            "1. Thinly slice half a small onion.\n"
            "2. Layer with honey in a clean jar; rest 1–2 hours (or overnight in the fridge).\n"
            "3. Take 1 tsp of the resulting syrup as needed for cough.\n"
            "4. Optional: add a little ginger juice to the mix."
        ),
        "benefits": "Folk kitchen remedy often used for stubborn coughs.",
        "precautions": "Strong taste/smell. Not for infants. Discontinue if stomach upset occurs.",
    },
]


def normalize_ingredient_name(name: str) -> str:
    return name.strip().lower()


def score_remedy(remedy: dict, selected_ingredients: list[str], ailment: str, dosha: str) -> tuple[int, list[str], list[str]]:
    """Return (score, matched_required, missing_required)."""
    selected = {normalize_ingredient_name(i) for i in selected_ingredients}
    required = remedy["required"]
    helpful = remedy.get("helpful", [])

    matched_required = [r for r in required if normalize_ingredient_name(r) in selected]
    missing_required = [r for r in required if normalize_ingredient_name(r) not in selected]
    matched_helpful = [h for h in helpful if normalize_ingredient_name(h) in selected]

    score = 0
    # Ailment match is mandatory filter elsewhere; still weight it
    if ailment in remedy["ailments"]:
        score += 50
    if dosha in remedy["doshas"] or dosha == "Not sure / Tridoshic":
        score += 15
    # Ingredient coverage
    if required:
        score += int(40 * (len(matched_required) / len(required)))
    score += min(15, 5 * len(matched_helpful))
    # Prefer fully makeable remedies
    if not missing_required:
        score += 25

    return score, matched_required, missing_required


def find_remedies(
    ailment: str,
    dosha: str,
    selected_ingredients: list[str],
    allow_partial: bool,
    top_n: int = 5,
) -> list[dict]:
    results = []
    for remedy in REMEDIES:
        if ailment not in remedy["ailments"]:
            continue
        if dosha not in remedy["doshas"] and dosha != "Not sure / Tridoshic":
            # Still allow if tridoshic-tagged or user unsure handled above
            if "Not sure / Tridoshic" not in remedy["doshas"]:
                continue

        score, matched_required, missing_required = score_remedy(
            remedy, selected_ingredients, ailment, dosha
        )
        if not allow_partial and missing_required:
            continue
        if allow_partial and len(matched_required) == 0 and missing_required:
            # Need at least some overlap unless user selected nothing — then show all for ailment
            if selected_ingredients:
                continue

        results.append(
            {
                **remedy,
                "score": score,
                "matched_required": matched_required,
                "missing_required": missing_required,
            }
        )

    results.sort(key=lambda r: r["score"], reverse=True)
    return results[:top_n]


def render_remedy(remedy: dict, rank: int) -> None:
    can_make = not remedy["missing_required"]
    status = "Ready with your cabinet" if can_make else "Almost — missing a few items"
    st.markdown(
        f"""
        <div class="remedy-card">
            <h3 style="margin-top:0;color:#2d5a27;">{rank}. {remedy['title']}</h3>
            <p><span class="match-badge">{status}</span>
            <span class="match-badge">Match {remedy['score']}%</span></p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("**Uses your:**")
        if remedy["matched_required"]:
            st.write(", ".join(remedy["matched_required"]))
        else:
            st.write("—")
        helpful_have = [
            h
            for h in remedy.get("helpful", [])
            if normalize_ingredient_name(h)
            in {normalize_ingredient_name(x) for x in st.session_state.get("selected_ingredients", [])}
        ]
        if helpful_have:
            st.caption("Also boosted by: " + ", ".join(helpful_have))
    with col_b:
        if remedy["missing_required"]:
            st.markdown("**Still need:**")
            st.write(", ".join(remedy["missing_required"]))
        else:
            st.markdown("**Still need:**")
            st.write("Nothing — you're set.")

    st.markdown("**How to prepare**")
    st.markdown(remedy["method"])
    st.markdown(f"**Why it helps:** {remedy['benefits']}")
    st.markdown(f"**Precautions:** {remedy['precautions']}")
    st.markdown(
        f"**Best for doshas:** {', '.join(d for d in remedy['doshas'] if d != 'Not sure / Tridoshic')}"
    )
    st.divider()


# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------
st.markdown(
    '<p class="main-title">🌿 Kitchen Cabinet Ayurvedic Remedy Generator</p>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p class="subtitle">Turn everyday spices and pantry staples into simple Ayurvedic home remedies.</p>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="disclaimer">
    <strong>Educational use only.</strong> This app shares traditional kitchen-remedy ideas for learning and
    self-care inspiration. It is <em>not</em> medical advice, diagnosis, or treatment.
    Consult a qualified healthcare professional or Ayurvedic practitioner for personal concerns,
    pregnancy, chronic conditions, or emergencies.
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

with st.sidebar:
    st.header("Your profile")
    dosha = st.selectbox(
        "Dominant dosha (if known)",
        DOSHAS,
        index=3,
        help="Ayurveda describes three mind-body patterns: Vata, Pitta, and Kapha.",
    )
    st.markdown("---")
    st.caption(
        "Tip: Select the ingredients you actually have. "
        "Enable partial matches to see remedies you nearly have."
    )
    st.markdown("### Quick pantry presets")
    if st.button("Common Indian kitchen"):
        st.session_state["preset"] = [
            "Turmeric (Haldi)",
            "Ginger (Adrak)",
            "Cumin (Jeera)",
            "Coriander (Dhania)",
            "Fennel (Saunf)",
            "Black Pepper (Kali Mirch)",
            "Honey",
            "Ghee",
            "Lemon",
            "Milk",
            "Yogurt / Curd",
            "Garlic",
            "Ajwain (Carom Seeds)",
            "Asafoetida (Hing)",
            "Holy Basil / Tulsi",
            "Cinnamon (Dalchini)",
            "Cardamom (Elaichi)",
            "Clove (Laung)",
        ]
    if st.button("Clear selection"):
        st.session_state["preset"] = []

default_selection = st.session_state.get(
    "preset",
    ["Turmeric (Haldi)", "Ginger (Adrak)", "Honey", "Lemon", "Cumin (Jeera)"],
)

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("1. How can we help?")
    ailment = st.selectbox("Primary concern", AILMENTS, index=0)
    allow_partial = st.checkbox(
        "Include remedies I'm missing ingredients for",
        value=True,
        help="When checked, you'll also see near-matches and shopping hints.",
    )

with col2:
    st.subheader("2. What's in your kitchen cabinet?")
    selected_ingredients = st.multiselect(
        "Available ingredients",
        options=INGREDIENTS,
        default=[i for i in default_selection if i in INGREDIENTS],
        help="Select everything you can use today.",
    )
    st.session_state["selected_ingredients"] = selected_ingredients

st.subheader("3. Generate remedies")
generate = st.button("Generate Ayurvedic Remedies", type="primary", use_container_width=False)

if generate:
    if not selected_ingredients and not allow_partial:
        st.warning("Select at least one ingredient, or enable partial matches.")
    else:
        matches = find_remedies(
            ailment=ailment,
            dosha=dosha,
            selected_ingredients=selected_ingredients,
            allow_partial=allow_partial or not selected_ingredients,
            top_n=6,
        )
        if not matches:
            st.info(
                "No remedies matched your filters. Try enabling partial matches, "
                "choosing another concern, or adding more pantry items."
            )
        else:
            st.success(
                f"Found {len(matches)} remedy idea(s) for **{ailment}** "
                f"(dosha focus: **{dosha}**)."
            )
            for idx, remedy in enumerate(matches, start=1):
                # Display score as a friendlier 0–100 style number
                remedy = {**remedy, "score": min(99, remedy["score"])}
                render_remedy(remedy, idx)

            with st.expander("Ayurveda basics (quick reference)"):
                st.markdown(
                    """
                    - **Vata** (air + ether): movement, dryness, irregularity — favors warm, moist, grounding foods.
                    - **Pitta** (fire + water): transformation, heat — favors cooling, moderate, non-spicy support.
                    - **Kapha** (earth + water): structure, stability — favors light, warm, stimulating spices.

                    Kitchen spices are often the first pharmacy in classical home care:
                    turmeric for inflammation, ginger for agni, cumin/coriander/fennel for digestion,
                    tulsi for respiratory comfort, and ghee/milk for nourishment.
                    """
                )

st.markdown("---")
st.caption(
    "Kitchen Cabinet Ayurvedic Remedy Generator · Traditional home-remedy inspiration · Not a substitute for professional care"
)
