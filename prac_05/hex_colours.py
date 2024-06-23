COLOUR_NAMES = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "	#f0f8ff",
                "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Beige": "#f5f5dc",
                "Champagne": "#f7e7ce", "Charcoal": "#36454f", "Cobalt": "#0047ab", "Coffee": "#6f4e37"}
valid_colours = {name.lower(): colour.lower() for name, colour in COLOUR_NAMES.items()}

choice = input("Valid Colours:").lower()
while choice != "":
    print(f"The color code for {choice} is {valid_colours[choice]}")
    choice = input("Valid Colours:").lower()


