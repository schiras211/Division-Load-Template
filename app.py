import streamlit as st
from pathlib import Path
import pandas as pd

st.set_page_config(
page_title="Dallas Wrightsoft Guide",
layout="wide"
)

# ---------------- STYLE ----------------

st.markdown("""

<style>
[data-testid="stSidebar"] {
    background-color: #EEF3F8;
    padding-top: 25px;
}

.main-header {
    background-color: #003E7E;
    color: white;
    padding: 28px 32px;
    margin: -60px -80px 25px -80px;
}

.main-header h1 {
    font-size: 38px;
    margin: 0;
}

.main-header p {
    font-size: 18px;
    margin-top: 8px;
}

.step-card {
    background: white;
    border-radius: 18px;
    box-shadow: 0 4px 16px rgba(0,0,0,.15);
    overflow: hidden;
    border: 1px solid #D0D7DE;
}

.step-header {
    background: #003E7E;
    color: white;
    padding: 18px 24px;
    font-size: 28px;
    font-weight: bold;
}

.step-body {
    padding: 24px;
}

.note-box {
    background: #FFF200;
    color: black;
    padding: 12px 16px;
    border-radius: 8px;
    font-weight: 800;
    margin-bottom: 14px;
    border: 1px solid #D9C900;
}

.stExpander {
    background-color: #EEF3F8;
    border: 1px solid #BFD0DF;
    border-radius: 10px;
    margin-bottom: 12px;
}

.stExpander summary {
    font-size: 18px;
    font-weight: 700;
}

img {
    border-radius: 10px;
}
</style>

""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown("""

<div class="main-header">
    <h1>Dallas Wrightsoft Load Completion Guide</h1>
    <p>Interactive Navigation Guide</p>
</div>
""", unsafe_allow_html=True)

# ---------------- DATA ----------------

steps = {
"STEP 1 - Project Setup & Notes": {
"items": [
{
"title": "Contact POC if help is needed.",
"details": [
"If an example or clarification is needed, contact the Dallas POC.",
"Do not overwork the file if the setup is unclear."
],
"images": []
},
{
"title": "Use Dallas matchups.",
"details": [
"Use Dallas-specific matchup rules when selecting equipment.",
"Verify equipment selections before finalizing the load."
],
"images": []
},
{
"title": "Add selected elevation in Project Information notes.",
"details": [
"In Project Information notes, add the elevation selected for the load.",
"This helps Sales understand which elevation was used."
],
"images": []
},
{
"title": "Lennox BTU adjustment rule.",
"details": [
"When adding BTUs to Lennox loads, increase blower power between 500–750 first.",
"Add more BTUs only if still needed after blower adjustment.",
"Do not exceed 750 for the blower adjustment."
],
"images": []
},
{
"title": "Use 360 CFM per ton.",
"details": [
"Use 360 CFM per ton as the airflow rule for this Dallas workflow."
],
"images": []
},
{
"title": "Select correct template.",
"details": [
"Start with the correct Wrightsoft template for the project.",
"Verify template before entering load details."
],
"images": []
},
{
"title": "Keep humidity set to 30/50.",
"details": [
"Do not change the humidity setting unless instructed by project-specific requirements."
],
"images": []
},
{
"title": "Zone all 2-story homes.",
"details": [
"All 2-story homes should be zoned."
],
"images": []
}
]
},

```
"STEP 2 - Weather, County & Ceiling Setup": {
    "items": [
        {
            "title": "Select the correct weather location for every project.",
            "details": [
                "Use the weather location listed on the plan or spec sheet.",
                "Do not assume the nearest major city is correct."
            ],
            "images": [
                "screenshots/weather_location.png"
            ]
        },
        {
            "title": "Verify the county using Energy Star.",
            "details": [
                "When required, verify the county using the Energy Star website.",
                "Use the county-specific data to confirm weather requirements."
            ],
            "images": [
                "screenshots/energy_star_county.png"
            ]
        },
        {
            "title": "Adjust annual cooling and heating dry bulb temperatures.",
            "details": [
                "Adjust annual cooling and heating dry bulb temperatures to match the specified county.",
                "Use Bin City Data to select the correct weather station."
            ],
            "images": [
                "screenshots/bin_city_data.png"
            ]
        },
        {
            "title": "Select the correct weather station under Bin City Data.",
            "details": [
                "Open Bin City Data.",
                "Select the weather station that matches the required county/weather location."
            ],
            "images": [
                "screenshots/weather_station.png"
            ]
        },
        {
            "title": "Foam ceiling insulation setup.",
            "details": [
                "For foam custom ceiling insulation, place the configuration under Roof/Ceiling.",
                "Do not treat foam ceiling projects the same as standard ceiling insulation."
            ],
            "images": [
                "screenshots/foam_ceiling.png"
            ]
        },
        {
            "title": "Non-foam ceiling setup.",
            "details": [
                "For non-foam ceiling insulation, leave the standard ceiling setup as shown."
            ],
            "images": [
                "screenshots/non_foam_ceiling.png"
            ]
        }
    ]
},

"STEP 3 - Options & In-Lieu Rooms": {
    "items": [
        {
            "title": "Use parentheses for option rooms.",
            "details": [
                "When placing options on a load, use the optional room as the title and place the option in parentheses.",
                "Example: Flex(Study)."
            ],
            "images": []
        },
        {
            "title": "Apply worst-case BTUH to in-lieu rooms.",
            "details": [
                "If Study is in lieu of Flex and Study is the worst case, use the Study BTUH for Flex(Study).",
                "If the Study windows are worse, include those windows in the load."
            ],
            "images": []
        },
        {
            "title": "Add selected elevation floors into CAD.",
            "details": [
                "If the selected elevation has a floor, add it to CAD so the drawing reflects accuracy."
            ],
            "images": []
        },
        {
            "title": "Match base tonnage when possible.",
            "details": [
                "If there is an option, try to match the tonnage from the base.",
                "If not possible, notify the POC."
            ],
            "images": []
        }
    ]
},

"STEP 4 - Room Load Rules": {
    "items": [
        {
            "title": "No blinds on loads.",
            "details": [
                "Do not apply blinds to Dallas loads."
            ],
            "images": []
        },
        {
            "title": "Use R-3 exterior board insulation when specified.",
            "details": [
                "Sheathing 3/8: if R-3 sheathing is on the specs, select exterior board insulation R-3."
            ],
            "images": []
        },
        {
            "title": "Merge WIC rooms unless master WIC has a window.",
            "details": [
                "Merge all WIC rooms unless the master WIC has a window.",
                "If the master WIC has a window, the WIC should be its own room.",
                "Do not use the 10 ft exposure rule for WIC rooms."
            ],
            "images": []
        },
        {
            "title": "Make foyers separate rooms.",
            "details": [
                "Foyers should be their own room, even if they are very short."
            ],
            "images": []
        },
        {
            "title": "Merge pantry with kitchen unless heat load exists.",
            "details": [
                "Always merge pantry with kitchen unless it has a window or heat load.",
                "Examples of heat load include fridge, stove, or similar appliance."
            ],
            "images": []
        },
        {
            "title": "Align rooms accurately to walls.",
            "details": [
                "Place rooms as accurately as possible.",
                "Line rooms up to walls unless additional square footage is needed."
            ],
            "images": []
        }
    ]
},

"STEP 5 - CAD Cleanup": {
    "items": [
        {
            "title": "Clean electrical items but leave lights/fans.",
            "details": [
                "Clean as much electrical information as possible.",
                "Leave lights and fans visible so boot placement can be accurate."
            ],
            "images": [
                "screenshots/CAD Conversion.png"
            ]
        },
        {
            "title": "Add all options into CAD.",
            "details": [
                "If options exist, place the options in CAD.",
                "This is needed for future design and load accuracy."
            ],
            "images": [
                "screenshots/CAD Conversion 2.png"
            ]
        },
        {
            "title": "Use one CAD file with correct elevation and options.",
            "details": [
                "Do not create separate scattered files.",
                "Use one CAD file with the correct elevation and all options included."
            ],
            "images": []
        },
        {
            "title": "Only set specific rooms to ambient when needed.",
            "details": [
                "If the load has a lip, do not change the whole floor to ambient.",
                "Only change the specific rooms needed."
            ],
            "images": []
        }
    ]
},

"STEP 6 - Equipment Matchups & Airflow": {
    "items": [
        {
            "title": "Select correct equipment matchups.",
            "details": [
                "Select the correct matchups when placing equipment.",
                "Verify matchups before final equipment selection."
            ],
            "images": []
        },
        {
            "title": "Lennox blower power first.",
            "details": [
                "For Lennox, increase blower power 500–750 before adding BTUH.",
                "Do not exceed 750 blower adjustment."
            ],
            "images": []
        },
        {
            "title": "Line up spiral cases and OTB accurately.",
            "details": [
                "If spiral cases and OTB are present, line both up accurately with the plan."
            ],
            "images": []
        },
        {
            "title": "Merge CFMs for outdoor air with two systems.",
            "details": [
                "Merge CFMs for outdoor air when two systems are used."
            ],
            "images": []
        },
        {
            "title": "Use worst-case windows on base load.",
            "details": [
                "Bay windows and box windows should be placed on the base load as worst case."
            ],
            "images": []
        },
        {
            "title": "Use custom R-value if not listed.",
            "details": [
                "If an R-value is not listed, use a custom R-value.",
                "Contact the POC if help is needed."
            ],
            "images": []
        },
        {
            "title": "Static pressure values.",
            "details": [
                "Gas static pressure = .70.",
                "Heat pump static pressure = .50."
            ],
            "images": []
        },
        {
            "title": "Save Lennox documentation.",
            "details": [
                "For Lennox, save the Word document showing the math, expanded ratings, and manufacturer numbers."
            ],
            "images": []
        }
    ]
},

"STEP 7 - Internal Gains": {
    "table": [
        ["Bedroom", "1 person"],
        ["Owner Suite", "2 people + Min 500 / Max 1000"],
        ["Great Room / Family", "Min 900 / Max 1800"],
        ["Kitchen < 3 Large Appliances", "Min 1200 / Max 2400"],
        ["Kitchen > 3 Large Appliances", "Min 2000 / Max 4000"],
        ["Bar", "Min 600 / Max 1200"],
        ["Utility / Laundry", "Min 500 / Max 1000"],
        ["Media / Theater", "Min 1200 / Max 2400"],
        ["Loft / Game / Bonus", "Min 900 / Max 1800"],
        ["Study / Library / Office", "Min 600 / Max 1200"],
        ["Exercise", "Min 600 / Max 1200"],
        ["Room with Refrigerator / Freezer", "Add Min 600 / Max 1200"]
    ]
},

"STEP 8 - Equipment Sizing": {
    "items": [
        {
            "title": "100%–104% total capacity rule.",
            "details": [
                "When a unit is at 100%–104% total, and sometimes 105%, attempt to go up 1/2 ton and add BTUs to fit at 115%."
            ],
            "images": []
        },
        {
            "title": "100% total often upgrades to next ton.",
            "details": [
                "If total is 100%, usually upgrade to the next ton, especially on Lennox systems."
            ],
            "images": []
        },
        {
            "title": "Do not upsize if it creates 122%–124%.",
            "details": [
                "If upsizing causes total to exceed 122%–124% or requires a lot of added BTUH, do not upsize."
            ],
            "images": []
        },
        {
            "title": "Use sq ft per ton as secondary guidance.",
            "details": [
                "Standard homes: 600–700 sq ft per ton.",
                "Foam homes: 700–800 sq ft per ton.",
                "These are rules of thumb, not standards."
            ],
            "images": []
        },
        {
            "title": "105% total / 98% sensible example.",
            "details": [
                "If a load gives 105% total and 98% sensible, do not upgrade the tonnage.",
                "Leave the current tonnage as-is."
            ],
            "images": []
        }
    ]
},

"STEP 9 - Open To Below": {
    "items": [
        {
            "title": "Set OTB only in required areas.",
            "details": [
                "Set open to below in required areas and verify that square footage is within range."
            ],
            "images": []
        },
        {
            "title": "Preferred OTB area is under 100 sq ft.",
            "details": [
                "Preferred OTB area is under 100 sq ft.",
                "If square footage is needed, bump the walls out slightly on all floors."
            ],
            "images": []
        },
        {
            "title": "Remove OTB before equipment selection.",
            "details": [
                "Afterward, remove open to below and set what is upstairs and downstairs in their proper areas before selecting equipment."
            ],
            "images": []
        },
        {
            "title": "Boot placement at OTB.",
            "details": [
                "Use OTB for square footage only, then turn it back to a regular room.",
                "A boot will be placed on that OTB area: 1 up and 1 down."
            ],
            "images": []
        }
    ]
},

"STEP 10 - Blower Door Settings": {
    "items": [
        {
            "title": "Beazer blower door setup.",
            "details": [
                "Select the fireplace first, then start blower door setup.",
                "Wind shielding: 3.",
                "Select Single @ Test Pressure.",
                "ACH: 1.5.",
                "Test pressure difference: 50 Pascals."
            ],
            "images": []
        },
        {
            "title": "D.R. Horton East blower door setup.",
            "details": [
                "Settings depend on specs.",
                "Select the fireplace first, then start blower door setup.",
                "Wind shielding: 3.",
                "Select Single @ Test Pressure.",
                "ACH: 3.",
                "Test pressure difference: 50 Pascals."
            ],
            "images": []
        }
    ]
},

"STEP 11 - Energy Star": {
    "items": [
        {
            "title": "Location and control settings.",
            "details": [
                "Use location by county.",
                "Control Location: Attic/Mech."
            ],
            "images": []
        },
        {
            "title": "Fresh air and humidity settings.",
            "details": [
                "Fresh Air Settings: 20/60.",
                "Relative Humidity: 30/50.",
                "Beazer Estar: 60/60."
            ],
            "images": []
        },
        {
            "title": "Fin-180P airflow range.",
            "details": [
                "Fin-180P cycle range should be 130 CFM–180 CFM, rounded to the nearest value.",
                "Run Time Per Cycle is the only number that can be changed to stay within the required vent airflow range."
            ],
            "images": []
        }
    ]
},

"STEP 12 - Save & Handoff": {
    "items": [
        {
            "title": "Save the load.",
            "details": [
                "Save the load before handoff."
            ],
            "images": []
        },
        {
            "title": "POC completes PDF portion.",
            "details": [
                "The POC will complete the PDF portion.",
                "The POC will update this guide as more information becomes available."
            ],
            "images": []
        },
        {
            "title": "Dallas Division POC.",
            "details": [
                "If questions remain, contact the Dallas Division POC.",
                "Dallas Division POC: Alberto Hernandez."
            ],
            "images": []
        }
    ]
}
```

}

# ---------------- SIDEBAR ----------------

st.sidebar.markdown("## Table of Contents")

step_names = list(steps.keys())

if "step_index" not in st.session_state:
st.session_state.step_index = 0

selected_step = st.sidebar.radio(
"Select Step",
step_names,
index=st.session_state.step_index,
label_visibility="collapsed"
)

st.session_state.step_index = step_names.index(selected_step)

# ---------------- MAIN LAYOUT ----------------

left, right = st.columns([1.25, 1])

with left:
st.markdown(f""" <div class="step-card"> <div class="step-header">{selected_step}</div> <div class="step-body">
""", unsafe_allow_html=True)

```
if selected_step == "STEP 1 - Project Setup & Notes":
    st.markdown("""
    <div class="note-box">
        IF NEED EXAMPLE OR HELP CONTACT POC. PLEASE DO NOT OVERWORK.
    </div>
    """, unsafe_allow_html=True)

current_step = steps[selected_step]

if "items" in current_step:
    for item in current_step["items"]:
        with st.expander("• " + item["title"]):
            for detail in item["details"]:
                st.write("• " + detail)

            for img in item.get("images", []):
                if Path(img).exists():
                    st.image(img, use_container_width=True)
                else:
                    st.info(f"Screenshot not uploaded yet: {img}")

if "table" in current_step:
    df = pd.DataFrame(
        current_step["table"],
        columns=["Room Type", "Internal Gains"]
    )

    st.table(df)

st.markdown("</div></div>", unsafe_allow_html=True)
```

with right:
st.markdown("## Page Screenshot Area")

```
st.info(
    "Click an item on the left to expand detailed instructions and item-specific screenshots."
)
```

# ---------------- BUTTONS ----------------

st.markdown("<br>", unsafe_allow_html=True)

btn1, btn2, btn3 = st.columns([1, 5, 1])

with btn1:
if st.button("Top"):
st.session_state.step_index = 0
st.rerun()

with btn3:
if st.button("Next →"):
if st.session_state.step_index < len(step_names) - 1:
st.session_state.step_index += 1
st.rerun()

