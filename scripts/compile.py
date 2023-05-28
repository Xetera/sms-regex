import json
import yaml


if __name__ == "__main__":
    print("Compiling patterns.yaml to patterns.json")
    out = yaml.load(
        open("./patterns.yaml", "r"),
        Loader=yaml.CLoader
    )
    json.dump(out, open("./patterns.json", "w"), indent=2)
    print("Done!")
