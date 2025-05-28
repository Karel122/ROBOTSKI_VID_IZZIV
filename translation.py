import json

# Define your event name mapping
event_mapping = {
    "prazna_roka": "empty hand",
    "prijemanje_pina": "grabbing the pin",
    "odlaganje_pina": "putting in a hole",
    "prenos_pina": "carring the pin"
}

# Load your original JSON
with open("your_file.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Replace event names based on the mapping
for annotation in data["annotations"]:
    event_name = annotation["event"]
    if event_name in event_mapping:
        annotation["event"] = event_mapping[event_name]

# Save the updated JSON
with open("updated_file.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Event names updated successfully.")
