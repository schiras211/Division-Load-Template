import streamlit as st
from pathlib import Path
import pandas as pd

st.set_page_config(
    page_title="Wrightsoft Division Guides",
    layout="wide"
)

# ---------------- STYLE ---------------- #

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
    margin-bottom: 25px;
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

.warning-box {
    background: #FFE5E5;
    color: #7A0000;
    padding: 12px 16px;
    border-radius: 8px;
    font-weight: 700;
    margin: 12px 0;
    border: 1px solid #CC0000;
}

.example-box {
    background: #EAF4FF;
    color: #003E7E;
    padding: 12px 16px;
    border-radius: 8px;
    font-weight: 600;
    margin: 12px 0;
    border: 1px solid #9CC9F5;
}

.rule-box {
    background: #F2F7F2;
    color: #1F5B2E;
    padding: 12px 16px;
    border-radius: 8px;
    font-weight: 600;
    margin: 12px 0;
    border: 1px solid #B7D8B7;
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
    border: 1px solid #D0D7DE;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HELPERS ---------------- #

def show_images(images):
    for img in images:
        if Path(img).exists():
            st.image(img, use_container_width=True)
        else:
            st.info(f"Screenshot not uploaded yet: {img}")

def bullet_list(items):
    for item in items:
        st.write("• " + item)

def make_placeholder_steps(division_name, folder_name):
    return {
        "STEP 1 - CAD Cleanup": {
            "items": [
                {
                    "title": f"{division_name} CAD cleanup rule",
                    "rule": f"Add {division_name}-specific CAD cleanup rules here.",
                    "details": [
                        "Add division-specific CAD cleanup notes.",
                        "Add screenshot references as needed."
                    ],
                    "images": [f"screenshots/{folder_name}/example.png"]
                }
            ]
        },
        "STEP 2 - Project Setup & Notes": {
            "items": [
                {
                    "title": f"{division_name} project setup rule",
                    "rule": f"Add {division_name}-specific project setup rules here.",
                    "details": [
                        "Add template, notes, airflow, zoning, and POC rules here."
                    ],
                    "images": []
                }
            ]
        },
        "STEP 3 - Weather, County & Ceiling Setup": {
            "items": [
                {
                    "title": f"{division_name} weather setup",
                    "rule": "Add weather, county, and ceiling setup rules here.",
                    "details": [
                        "Add Energy Star, county, weather station, foam, and non-foam rules."
                    ],
                    "images": []
                }
            ]
        },
        "STEP 4 - Options & In-Lieu Rooms": {
            "items": [
                {
                    "title": f"{division_name} option room rules",
                    "rule": "Add option and in-lieu room rules here.",
                    "details": [
                        "Add naming, worst-case BTUH, windows, and option tonnage rules."
                    ],
                    "images": []
                }
            ]
        },
        "STEP 5 - Room Load Rules": {
            "items": [
                {
                    "title": f"{division_name} room load rules",
                    "rule": "Add room-specific load rules here.",
                    "details": [
                        "Add WIC, pantry, foyer, blinds, insulation, and room placement rules."
                    ],
                    "images": []
                }
            ]
        },
        "STEP 6 - Open To Below": {
            "items": [
                {
                    "title": f"{division_name} OTB rules",
                    "rule": "Add open-to-below rules here.",
                    "details": [
                        "Add square footage, temporary OTB, and boot placement rules."
                    ],
                    "images": []
                }
            ]
        },
        "STEP 7 - Blower Door Settings": {
            "items": [
                {
                    "title": f"{division_name} blower door setup",
                    "rule": "Add blower door setup rules here.",
                    "details": [
                        "Add ACH, wind shielding, test pressure, and builder-specific settings."
                    ],
                    "images": []
                }
            ]
        },
        "STEP 8 - Energy Star": {
            "items": [
                {
                    "title": f"{division_name} Energy Star setup",
                    "rule": "Add Energy Star setup rules here.",
                    "details": [
                        "Add fresh air, humidity, county, control location, and ventilation rules."
                    ],
                    "images": []
                }
            ]
        },
        "STEP 9 - Equipment Matchups, Airflow & Special Conditions": {
            "items": [
                {
                    "title": f"{division_name} equipment matchup rules",
                    "rule": "Add equipment matchup and airflow rules here.",
                    "details": [
                        "Add matchup, static pressure, airflow, manufacturer, and documentation rules."
                    ],
                    "images": []
                }
            ]
        },
        "STEP 10 - Equipment Sizing": {
            "items": [
                {
                    "title": f"{division_name} equipment sizing rules",
                    "rule": "Add equipment sizing rules here.",
                    "details": [
                        "Add total capacity, sensible capacity, tonnage, and sq ft per ton rules."
                    ],
                    "images": []
                }
            ]
        },
        "STEP 11 - Internal Gains": {
            "table": [
                ["Bedroom", "Add division-specific value"],
                ["Owner Suite", "Add division-specific value"],
                ["Great Room / Family", "Add division-specific value"],
                ["Kitchen", "Add division-specific value"],
                ["Utility / Laundry", "Add division-specific value"],
                ["Study / Office", "Add division-specific value"]
            ],
            "notes": [
                f"Add {division_name}-specific internal gain rules here."
            ]
        },
        "STEP 12 - Save & Handoff": {
            "items": [
                {
                    "title": f"{division_name} save and handoff",
                    "rule": "Add final save and handoff rules here.",
                    "details": [
                        "Add POC, PDF, review, and final completion rules."
                    ],
                    "images": []
                }
            ]
        }
    }

# ---------------- HEADER ---------------- #

st.markdown("""
<div class="main-header">
    <h1>Wrightsoft Load Completion Guides</h1>
    <p>Division-Specific Interactive Workflow</p>
</div>
""", unsafe_allow_html=True)

# ---------------- CINCINNATI / DAYTON DATA ---------------- #

cincinnati_dayton_steps = {
    "STEP 1 - CAD Cleanup": {
        "items": [
            {
                "title": "Garage setup",
                "rule": "Draw the garage as a room, then remove it from the calculations.",
                "details": [
                    "Heating: none.",
                    "Cooling: none.",
                    "Use this unless the Builder Spec Sheet states differently."
                ],
                "images": []
            },
            {
                "title": "Open to below setup",
                "rule": "Only make Open To Below if it has closed walls surrounding it.",
                "details": [
                    "If the Open To Below has open railing, do not make it Open To Below.",
                    "Use the plan condition to determine if it is closed wall or open railing."
                ],
                "images": []
            },
            {
                "title": "Walkout basement wall override",
                "rule": "If there is a walkout basement, use the wall tool to override the walkout above-grade walls.",
                "details": [
                    "Finished basements, unfinished basements, crawl, and slab conditions need to match the project setup.",
                    "Walkout above-grade walls should not be treated the same as below-grade basement walls."
                ],
                "images": [
                    "screenshots/Cincinnati_Dayton/finished_basement.png",
                    "screenshots/Cincinnati_Dayton/unfinished_basement.png",
                    "screenshots/Cincinnati_Dayton/crawl.png",
                    "screenshots/Cincinnati_Dayton/slab.png"
                ]
            }
        ]
    },

    "STEP 2 - Project Setup & Notes": {
        "items": [
            {
                "title": "Zone only upon request",
                "rule": "Zone upon request only.",
                "details": [
                    "Do not automatically zone every home.",
                    "Only set zoning if requested in the job, plans, or specs."
                ],
                "images": []
            },
            {
                "title": "Outside air rule",
                "rule": "Do not use outside air unless required.",
                "details": [
                    "Outside Air: No by default.",
                    "Use outside air only for foam insulation, Energy Star, or if requested in specs."
                ],
                "images": []
            },
            {
                "title": "Reports included",
                "rule": "Include the required Cincinnati / Dayton reports.",
                "details": [
                    "Loads: Short Room Summary.",
                    "Equipment: ACCA Manual S Compliance Report.",
                    "Upon request: Energy Star Form, 310 HVAC Design.",
                    "LEED requires Energy Star, ACCA 310, and Manual D."
                ],
                "images": []
            }
        ]
    },

    "STEP 3 - Weather, County & Ceiling Setup": {
        "items": [
            {
                "title": "Sloped ceilings",
                "rule": "Sloped ceilings are not used by default.",
                "details": [
                    "Sloped Ceilings: No.",
                    "Wrightsoft reads 90-degree angles and does not read sloped walls correctly."
                ],
                "images": []
            },
            {
                "title": "Knee wall setup",
                "rule": "Knee walls are areas with attic on the opposing side.",
                "details": [
                    "Do not draw the attic in as a room.",
                    "Account for the attic condition using the wall tool and Knee Wall tab.",
                    "If there is a sloped roof in an 8 ft room and the knee wall is 5 ft tall, put the wall tool in at 8 ft tall.",
                    "If entered at 5 ft, Wrightsoft reads 5 ft of knee wall and 3 ft of regular outside wall."
                ],
                "images": [
                    "screenshots/Cincinnati_Dayton/knee_wall.png"
                ]
            },
            {
                "title": "Standard walls",
                "rule": "Change the outside wall type if it is not vinyl.",
                "details": [
                    "If there are multiple wall types, use the wall tool.",
                    "Use 2x4 wall for R-13 and R-15.",
                    "Use 2x6 wall for R-19 and R-21."
                ],
                "images": []
            }
        ]
    },

    "STEP 4 - Options & In-Lieu Rooms": {
        "items": [
            {
                "title": "Study / Library room classification",
                "rule": "Study / Library is none unless it qualifies as a bedroom.",
                "details": [
                    "Count as a bedroom only if it has a closet and egress window.",
                    "Also count as a bedroom if it is listed as optional bedroom."
                ],
                "images": []
            }
        ]
    },

    "STEP 5 - Room Load Rules": {
        "items": [
            {
                "title": "Blinds and insect screens",
                "rule": "Use blinds only on Bed, WIC, or Bathroom windows.",
                "details": [
                    "Blinds: Bed/WIC/Bathroom windows only.",
                    "Insect screens are left as they are on the template."
                ],
                "images": []
            },
            {
                "title": "Freezer / fridge internal gain",
                "rule": "Any room with a freezer, fridge, or under-counter fridge gets 600 BTU added.",
                "details": [
                    "Apply this to any applicable room.",
                    "This is in addition to the normal room internal gain."
                ],
                "images": []
            }
        ]
    },

    "STEP 6 - Open To Below": {
        "items": [
            {
                "title": "OTB closed wall rule",
                "rule": "Only create Open To Below when closed walls surround the opening.",
                "details": [
                    "If open railing surrounds the opening, do not create Open To Below.",
                    "Use the actual construction condition shown on the plan."
                ],
                "images": []
            }
        ]
    },

    "STEP 7 - Blower Door Settings": {
        "items": [
            {
                "title": "Green Building infiltration",
                "rule": "Use the correct ACH50 based on the project type.",
                "details": [
                    "Gut Rehab: 5 ACH50.",
                    "New Construction without exterior rigid insulation: 4 ACH50.",
                    "New Construction with exterior rigid insulation: 3 ACH50.",
                    "Go to Options > Infiltration Method > Blower Door.",
                    "Then go to Load > Infiltration > Single Point > Test Pressure Difference.",
                    "Input 50 PA.",
                    "Click Airflow from ACH box.",
                    "Input the correct ACH value."
                ],
                "images": [
                    "screenshots/Cincinnati_Dayton/infiltration_green_building.png"
                ]
            },
            {
                "title": "SOL / Think Green infiltration",
                "rule": "Set infiltration to Tight.",
                "details": [
                    "Use this for SOL / Think Green projects."
                ],
                "images": [
                    "screenshots/Cincinnati_Dayton/infiltration_sol_think_green.png"
                ]
            }
        ]
    },

    "STEP 8 - Energy Star": {
        "items": [
            {
                "title": "Ventilation",
                "rule": "Use ASHRAE 62.2-2010.",
                "details": [
                    "Set Energy Star paperwork to the corrected infiltration method.",
                    "Confirm ventilation setup before final reports."
                ],
                "images": [
                    "screenshots/Cincinnati_Dayton/ventilation.png"
                ]
            },
            {
                "title": "Duct loss",
                "rule": "Leave duct loss on default percentages and set leakage type to Energy Star.",
                "details": [
                    "Use this setup for Energy Star duct loss requirements."
                ],
                "images": [
                    "screenshots/Cincinnati_Dayton/duct_loss.png"
                ]
            },
            {
                "title": "LEED homes only",
                "rule": "LEED requires Energy Star, ACCA 310, and Manual D.",
                "details": [
                    "There are three LEED levels: Silver, Gold, Platinum.",
                    "Silver: 5-year tax abatement.",
                    "Gold: 10-year tax abatement.",
                    "Platinum: 15-year tax abatement.",
                    "Currently, the house must be located in the City limits of Cincinnati.",
                    "Use the correct template and default temperatures."
                ],
                "images": []
            },
            {
                "title": "LEED info needed before starting",
                "rule": "Collect all LEED project requirements before starting.",
                "details": [
                    "Ceiling insulation.",
                    "Wall insulation.",
                    "Zip board, typically R-3 foam board.",
                    "Window specs with .1 variance.",
                    "Direction of the house.",
                    "Type of fresh air: ERV, bath fan, ducted, etc.",
                    "Equipment based on LEED level.",
                    "Number of systems requested.",
                    "Keep supplies overhead on 2nd floor. If needed, ask for 2nd system.",
                    "Address if not listed on plans.",
                    "Thermostat type.",
                    "Size of hood vent.",
                    "Do not worry about makeup air unless specified.",
                    "LEED contractor is one of the most important items."
                ],
                "images": []
            }
        ]
    },

    "STEP 9 - Equipment Matchups, Airflow & Special Conditions": {
        "items": [
            {
                "title": "Select equipment",
                "rule": "Equipment varies based on LEED level and should stay within 100%-130%.",
                "details": [
                    "Review equipment selection based on the project type.",
                    "LEED level may impact equipment requirements."
                ],
                "images": []
            },
            {
                "title": "Manual D static pressure",
                "rule": "Use .5 for air handlers and .7 for gas furnaces.",
                "details": [
                    "External Static Pressure: .5 for air handlers.",
                    "External Static Pressure: .7 for gas furnaces.",
                    "Supply diffusers: .03.",
                    "Return grilles: .03.",
                    "Filter: .1 for gas systems.",
                    "Balancing damper: .03 if zoning system and/or manual dampers are used."
                ],
                "images": []
            },
            {
                "title": "Carrier / Bryant coil pressure drop",
                "rule": "For Carrier / Bryant gas furnaces, use the correct coil pressure drop value.",
                "details": [
                    "Carrier / Bryant air handlers: leave coil blank.",
                    "1.5 ton vertical: 0.18.",
                    "2 ton vertical/horizontal: 0.19 / 0.19.",
                    "2.5 ton vertical/horizontal: 0.23 / 0.23.",
                    "3 ton vertical/horizontal: 0.27 / 0.27.",
                    "3.5 ton vertical/horizontal: 0.29 / 0.29.",
                    "4 ton vertical/horizontal: 0.29 / 0.29.",
                    "5 ton vertical/horizontal: 0.31 / 0.31."
                ],
                "images": []
            }
        ]
    },

    "STEP 10 - Equipment Sizing": {
        "items": [
            {
                "title": "Equipment sizing range",
                "rule": "Equipment should generally be selected within 100%-130%.",
                "details": [
                    "Equipment will vary based on LEED level.",
                    "Confirm Manual S compliance report."
                ],
                "images": []
            }
        ]
    },

    "STEP 11 - Internal Gains": {
        "table": [
            ["Bedroom", "1 Person"],
            ["Owner's Suite", "2 People"],
            ["Great Room / Family Room", "900 BTU"],
            ["Kitchen", "1200 BTU"],
            ["Kitchen with Double Oven or Additional Appliances", "2000 BTU"],
            ["Utility / Laundry", "0 BTU"],
            ["Media / Theater", "900 BTU"],
            ["Loft / Game / Bonus Room", "0 BTU"],
            ["Study / Library", "None unless bedroom-qualified"],
            ["Room with Freezer / Fridge / Under-Counter Fridge", "Add 600 BTU"]
        ],
        "notes": [
            "Study / Library counts as bedroom only if it has closet and egress window or is listed as optional bedroom.",
            "Any room with freezer, fridge, or under-counter fridge gets 600 BTU added."
        ]
    },

    "STEP 12 - Save & Handoff": {
        "items": [
            {
                "title": "Final paperwork",
                "rule": "When finished, load paperwork needs to include required reports.",
                "details": [
                    "Loads: Short Room Summary.",
                    "Equipment: ACCA Manual S Compliance Report.",
                    "Upon request: Energy Star Form, 310 HVAC Design.",
                    "For LEED: Energy Star, ACCA 310, and Manual D."
                ],
                "images": []
            },
            {
                "title": "Manual D completion",
                "rule": "Do not forget to select the Duct System Summary while printing.",
                "details": [
                    "See Manual D instructions sheet.",
                    "Delete extra supplies so there is only 1 supply per room.",
                    "Click Right-D toolbar icon.",
                    "Click Duct Preferences.",
                    "Change all duct material fields to ShtMetl.",
                    "Uncheck Use Variable Friction Rate.",
                    "Click Static Pressure icon.",
                    "If prompted that info is automatically generated from RightDraw, click Options and uncheck Hotlink Drawing.",
                    "Warning: If changes are needed after un-hotlinking, you will have to start over."
                ],
                "warning": "After un-hotlinking, additional load drawing changes may require starting over.",
                "images": []
            }
        ]
    }
}

# ---------------- DALLAS DATA ---------------- #

dallas_steps = {
    "STEP 1 - CAD Cleanup": {
        "items": [
            {
                "title": "Clean electrical but leave lights and fans",
                "rule": "Clean as much electrical information as possible, but leave lights and fans.",
                "details": [
                    "Lights and fans help with boot placement.",
                    "Leaving these items makes the design more realistic.",
                    "Clean unnecessary electrical clutter so the drawing is readable."
                ],
                "example": "Leave lights and fans visible so boot placement can be accurate.",
                "images": ["screenshots/Dallas/CAD Conversion.png"]
            },
            {
                "title": "Add options into CAD",
                "rule": "If the project has options, put the options in CAD.",
                "details": [
                    "Options are needed for future design.",
                    "Options also help keep the load accurate.",
                    "Do not leave options out if they affect the selected load or future design."
                ],
                "images": ["screenshots/Dallas/CAD Conversion 2.png"]
            },
            {
                "title": "Use one CAD file",
                "rule": "It should be one file with the right elevation and options all in one.",
                "details": [
                    "Do not create multiple disconnected files for the same load.",
                    "The CAD should include the correct elevation and needed options in one file."
                ],
                "warning": "DO NOT create scattered separate files.",
                "images": ["screenshots/Dallas/do_not_do_this.png"]
            },
            {
                "title": "Only change specific rooms to ambient",
                "rule": "If the load has a lip, do not change the whole floor to ambient.",
                "details": [
                    "Only change the specific rooms that need to be ambient.",
                    "Do not apply ambient settings across the entire floor unless required."
                ],
                "images": []
            }
        ]
    },

    "STEP 2 - Project Setup & Notes": {
        "items": [
            {
                "title": "Contact Dallas POC if help is needed",
                "rule": "If you need an example or help, contact the Dallas POC. Do not overwork the file.",
                "details": [
                    "Use the POC when something is unclear.",
                    "Dallas Division POC: Alberto Hernandez."
                ],
                "warning": "PLEASE DO NOT OVERWORK THE FILE.",
                "images": []
            },
            {
                "title": "Use Dallas matchups",
                "rule": "Use Dallas-specific equipment matchups when selecting equipment.",
                "details": [
                    "Confirm the selected matchup before finalizing equipment.",
                    "Dallas matchups should guide final equipment selection."
                ],
                "images": []
            },
            {
                "title": "Add selected elevation to Project Information notes",
                "rule": "In Project Information notes, add which elevation was selected.",
                "details": [
                    "This helps Sales know which elevation was used.",
                    "This helps anyone reviewing the file understand the load basis."
                ],
                "example": "Load completed using Elevation B with selected options shown on plan.",
                "images": []
            },
            {
                "title": "Lennox blower power before adding BTUH",
                "rule": "When adding BTUs to Lennox loads, increase blower power first.",
                "details": [
                    "Increase blower power between 500-750 first.",
                    "If more capacity is still needed, then add BTUH.",
                    "Do not exceed 750."
                ],
                "images": []
            },
            {
                "title": "Use 360 CFM per ton",
                "rule": "Dallas loads should use 360 CFM per ton.",
                "details": [
                    "Verify airflow before final equipment selection."
                ],
                "images": []
            },
            {
                "title": "Keep humidity at 30/50",
                "rule": "Keep the standard Dallas humidity setup at 30/50.",
                "details": [
                    "Do not change unless directed by project-specific requirements."
                ],
                "images": []
            },
            {
                "title": "Zone all 2-story homes",
                "rule": "All 2-story homes should be zoned.",
                "details": [
                    "Confirm zoning before finalizing the load."
                ],
                "images": []
            }
        ]
    },

    "STEP 3 - Weather, County & Ceiling Setup": {
        "items": [
            {
                "title": "Select correct weather location",
                "rule": "Select the correct weather location if listed on the plan or spec sheet.",
                "details": [
                    "Do not assume the closest major city is correct.",
                    "Use the weather location shown on the plan or spec sheet."
                ],
                "images": ["screenshots/Dallas/weather_location.png"]
            },
            {
                "title": "Verify county using Energy Star",
                "rule": "Verify county on Energy Star when needed.",
                "details": [
                    "Adjust annual cooling and heating dry bulb temperatures to match the specified county.",
                    "Under Bin City Data, select the correct weather station."
                ],
                "images": ["screenshots/Dallas/energy_star_county.png"]
            },
            {
                "title": "Foam ceiling insulation setup",
                "rule": "Foam custom ceiling insulation should be placed under Roof/Ceiling.",
                "details": [
                    "Do not treat foam ceiling projects the same as non-foam projects."
                ],
                "images": ["screenshots/Dallas/foam_ceiling.png"]
            },
            {
                "title": "Non-foam ceiling setup",
                "rule": "If it is non-foam ceiling, leave it as shown in standard setup.",
                "details": [
                    "Only use foam configuration when foam is specified."
                ],
                "images": ["screenshots/Dallas/non_foam_ceiling.png"]
            }
        ]
    },

    "STEP 4 - Options & In-Lieu Rooms": {
        "items": [
            {
                "title": "Use parentheses for option rooms",
                "rule": "Place the optional room as the title and the option in parentheses.",
                "details": [
                    "This keeps the base room and option room tied together."
                ],
                "example": "Flex(Study)",
                "images": []
            },
            {
                "title": "Apply worst-case BTUH to in-lieu rooms",
                "rule": "Use the BTUH from the worst-case option room.",
                "details": [
                    "If Study is in lieu of Flex and Study is worse, use Study BTUH.",
                    "If Study windows are worse, include those windows."
                ],
                "images": []
            },
            {
                "title": "Add selected elevation floor into CAD",
                "rule": "If the elevation chosen has a floor, add it to CAD.",
                "details": [
                    "The drawing needs to reflect the selected elevation accurately."
                ],
                "images": []
            },
            {
                "title": "Match base tonnage for options when possible",
                "rule": "Try to match the tonnage that was on the base.",
                "details": [
                    "If not possible, notify the POC."
                ],
                "images": []
            }
        ]
    },

    "STEP 5 - Room Load Rules": {
        "items": [
            {
                "title": "No blinds on loads",
                "rule": "Do not apply blinds to Dallas loads.",
                "details": [
                    "Leave blinds off the load calculation."
                ],
                "images": []
            },
            {
                "title": "R-3 exterior board insulation",
                "rule": "If R-3 sheathing is on the specs, select exterior board insulation R-3.",
                "details": [
                    "This applies when specs show Sheathing 3/8 with R-3."
                ],
                "images": []
            },
            {
                "title": "WIC merge rule",
                "rule": "All WIC rooms should be merged unless the Master WIC has a window.",
                "details": [
                    "If Master WIC has a window, it becomes its own room.",
                    "Do not apply the 10 ft exposure rule to WIC rooms."
                ],
                "warning": "NO 10 FT EXPOSURE RULE FOR WIC ROOMS.",
                "images": []
            },
            {
                "title": "Foyers should be separate rooms",
                "rule": "Foyers should be their own room, even if very short.",
                "details": [
                    "Do not automatically merge foyer areas into nearby rooms."
                ],
                "images": []
            },
            {
                "title": "Pantry merge rule",
                "rule": "Pantry should merge with kitchen unless it has a window or heat load.",
                "details": [
                    "Heat load examples: refrigerator, freezer, stove, or similar appliance."
                ],
                "images": []
            }
        ]
    },

    "STEP 6 - Open To Below": {
        "items": [
            {
                "title": "Set OTB only where required",
                "rule": "Set open to below in required areas only.",
                "details": [
                    "Preferred OTB area is under 100 sq ft.",
                    "Verify square footage is within range."
                ],
                "images": []
            },
            {
                "title": "Remove OTB before equipment selection",
                "rule": "After OTB is used for square footage, remove it before selecting equipment.",
                "details": [
                    "Set upstairs and downstairs areas properly.",
                    "OTB is temporary for square footage setup."
                ],
                "images": []
            },
            {
                "title": "Boot placement for OTB",
                "rule": "Use OTB for square footage, then turn it back to regular room.",
                "details": [
                    "There should be 1 boot up and 1 boot down."
                ],
                "images": []
            }
        ]
    },

    "STEP 7 - Blower Door Settings": {
        "items": [
            {
                "title": "Beazer blower door setup",
                "rule": "Use Beazer infiltration setup when applicable.",
                "details": [
                    "Select fireplace first.",
                    "Wind shielding: 3.",
                    "Select Single @ Test Pressure.",
                    "ACH: 1.5.",
                    "Test pressure difference: 50 Pascals."
                ],
                "images": []
            },
            {
                "title": "D.R. Horton East blower door setup",
                "rule": "Use D.R. Horton East setup depending on specs.",
                "details": [
                    "Select fireplace first.",
                    "Wind shielding: 3.",
                    "Select Single @ Test Pressure.",
                    "ACH: 3.",
                    "Test pressure difference: 50 Pascals."
                ],
                "images": []
            }
        ]
    },

    "STEP 8 - Energy Star": {
        "items": [
            {
                "title": "Location and control setup",
                "rule": "Use location by county and proper control location.",
                "details": [
                    "Location: by county.",
                    "Control Location: Attic/Mech."
                ],
                "images": []
            },
            {
                "title": "Fresh air and humidity settings",
                "rule": "Use Dallas Energy Star fresh air and humidity settings.",
                "details": [
                    "Fresh air settings: 20/60.",
                    "Relative humidity: 30/50.",
                    "Beazer Estar: 60/60."
                ],
                "images": []
            },
            {
                "title": "Fin-180P airflow range",
                "rule": "Fin-180P cycle range should be between 130 CFM and 180 CFM.",
                "details": [
                    "Run Time Per Cycle is the only number you can change.",
                    "Adjust it to stay within required vent airflow range."
                ],
                "images": ["screenshots/Dallas/energy_star_fin180p.png"]
            }
        ]
    },

    "STEP 9 - Equipment Matchups, Airflow & Special Conditions": {
        "items": [
            {
                "title": "Select correct equipment matchups",
                "rule": "Select the correct Dallas matchups when placing equipment.",
                "details": [
                    "Confirm equipment is matched correctly before finalizing."
                ],
                "images": []
            },
            {
                "title": "Static pressure settings",
                "rule": "Use correct static pressure on equipment selection screen.",
                "details": [
                    "Gas static pressure: .70",
                    "Heat pump static pressure: .50"
                ],
                "images": []
            },
            {
                "title": "Lennox documentation requirement",
                "rule": "For Lennox, save Word document showing supporting equipment math.",
                "details": [
                    "Include math.",
                    "Include expanded ratings.",
                    "Include manufacturer numbers."
                ],
                "images": []
            }
        ]
    },

    "STEP 10 - Equipment Sizing": {
        "items": [
            {
                "title": "100%-104% total capacity rule",
                "rule": "When unit is 100%-104% total, sometimes 105%, attempt to go up 1/2 ton.",
                "details": [
                    "After going up 1/2 ton, add BTUs to fit at 115%."
                ],
                "images": []
            },
            {
                "title": "Do not upsize if it pushes too high",
                "rule": "If upsizing causes total to go above 122%-124%, do not upsize.",
                "details": [
                    "If you have to add a lot of BTUH, it is usually not worth it."
                ],
                "images": []
            },
            {
                "title": "Use sq ft per ton as secondary guidance",
                "rule": "Use square feet per ton as a rule of thumb, not a standard.",
                "details": [
                    "Standard homes: 600-700 sq ft per ton.",
                    "Foam homes: 700-800 sq ft per ton."
                ],
                "images": []
            },
            {
                "title": "105% total example",
                "rule": "If load gives 105% total, usually do not upgrade if next ton requires too much BTUH.",
                "example": "If load has 105% total and 98% sensible, do not upgrade tonnage.",
                "details": [
                    "Leave it how it is unless POC directs otherwise."
                ],
                "images": []
            }
        ]
    },

    "STEP 11 - Internal Gains": {
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
            ["Add for Room with Refrigerator / Freezer", "Min 600 / Max 1200"]
        ],
        "notes": [
            "Use Dallas internal gain table when entering room gains.",
            "Rooms with refrigerators or freezers require additional internal gain."
        ]
    },

    "STEP 12 - Save & Handoff": {
        "items": [
            {
                "title": "Save the load",
                "rule": "Save the load before final handoff.",
                "details": [
                    "Do not hand off without saving."
                ],
                "images": []
            },
            {
                "title": "POC completes PDF portion",
                "rule": "The POC will complete the PDF portion.",
                "details": [
                    "Estimator completes the load first."
                ],
                "images": []
            }
        ]
    }
}

# ---------------- OTHER DIVISION PLACEHOLDERS ---------------- #

northern_kentucky_steps = make_placeholder_steps("Northern Kentucky", "Northern_Kentucky")
columbus_steps = make_placeholder_steps("Columbus", "Columbus")
indianapolis_steps = make_placeholder_steps("Indianapolis", "Indianapolis")
louisville_steps = make_placeholder_steps("Louisville", "Louisville")
viccarone_steps = make_placeholder_steps("Viccarone", "Viccarone")
raleigh_steps = make_placeholder_steps("Raleigh", "Raleigh")
charlotte_steps = make_placeholder_steps("Charlotte", "Charlotte")
mid_atlantic_steps = make_placeholder_steps("Mid Atlantic", "Mid_Atlantic")
nashville_steps = make_placeholder_steps("Nashville", "Nashville")
houston_steps = make_placeholder_steps("Houston", "Houston")
san_antonio_steps = make_placeholder_steps("San Antonio", "San_Antonio")
austin_steps = make_placeholder_steps("Austin", "Austin")

# ---------------- DIVISION GUIDE STORAGE ---------------- #

division_guides = {
    "Cincinnati / Dayton": cincinnati_dayton_steps,
    "Northern Kentucky": northern_kentucky_steps,
    "Columbus": columbus_steps,
    "Indianapolis": indianapolis_steps,
    "Louisville": louisville_steps,
    "Viccarone": viccarone_steps,
    "Raleigh": raleigh_steps,
    "Charlotte": charlotte_steps,
    "Mid Atlantic": mid_atlantic_steps,
    "Nashville": nashville_steps,
    "Houston": houston_steps,
    "Dallas": dallas_steps,
    "San Antonio": san_antonio_steps,
    "Austin": austin_steps
}

# ---------------- SIDEBAR ---------------- #

st.sidebar.markdown("## Division")

selected_division = st.sidebar.selectbox(
    "Select Division",
    list(division_guides.keys())
)

steps = division_guides[selected_division]

st.sidebar.markdown("## Table of Contents")

step_names = list(steps.keys())

if "step_index" not in st.session_state:
    st.session_state.step_index = 0

if st.session_state.step_index >= len(step_names):
    st.session_state.step_index = 0

selected_step = st.sidebar.radio(
    "Select Step",
    step_names,
    index=st.session_state.step_index,
    label_visibility="collapsed"
)

st.session_state.step_index = step_names.index(selected_step)

# ---------------- MAIN LAYOUT ---------------- #

left, right = st.columns([1.35, .9])

with left:
    st.markdown(f"""
    <div class="step-card">
        <div class="step-header">{selected_division} | {selected_step}</div>
        <div class="step-body">
    """, unsafe_allow_html=True)

    current_step = steps[selected_step]

    if selected_division == "Dallas" and selected_step == "STEP 2 - Project Setup & Notes":
        st.markdown("""
        <div class="note-box">
            IF NEED EXAMPLE OR HELP CONTACT POC. PLEASE DO NOT OVERWORK.
        </div>
        """, unsafe_allow_html=True)

    if "items" in current_step:
        for item in current_step["items"]:
            with st.expander("• " + item["title"]):

                if item.get("rule"):
                    st.markdown(f"""
                    <div class="rule-box">
                        <strong>Rule:</strong> {item["rule"]}
                    </div>
                    """, unsafe_allow_html=True)

                if item.get("details"):
                    st.markdown("### Details")
                    bullet_list(item["details"])

                if item.get("example"):
                    st.markdown(f"""
                    <div class="example-box">
                        <strong>Example:</strong> {item["example"]}
                    </div>
                    """, unsafe_allow_html=True)

                if item.get("warning"):
                    st.markdown(f"""
                    <div class="warning-box">
                        <strong>Warning:</strong> {item["warning"]}
                    </div>
                    """, unsafe_allow_html=True)

                show_images(item.get("images", []))

    if "table" in current_step:
        st.markdown("### Internal Gains Table")

        df = pd.DataFrame(
            current_step["table"],
            columns=["Room Type", "Internal Gains"]
        )

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
            height=500
        )

        st.markdown("### Notes")
        bullet_list(current_step.get("notes", []))

    st.markdown("</div></div>", unsafe_allow_html=True)

with right:
    st.markdown("## Instructions")

    st.info(
        "Select a division from the dropdown, then click a step. Photos only appear inside the clickable dropdown sections."
    )

# ---------------- BUTTONS ---------------- #

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
