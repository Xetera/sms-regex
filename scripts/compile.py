import json
import yaml

DESTINATION = "./generated/patterns.json"

if __name__ == "__main__":
    print(f"Compiling patterns.yaml to {DESTINATION}")
    with open("./patterns.yaml", "r", encoding="utf-8") as y,\
         open(DESTINATION, "w", encoding="utf-8") as j:
        out = yaml.load(y, Loader=yaml.CLoader)
        json.dump(out, j, indent=2)
        print("Done!")
