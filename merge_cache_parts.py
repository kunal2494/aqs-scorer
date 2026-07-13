import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
main_cache_path = os.path.join(SCRIPT_DIR, "search_cache.json")

print("Merging search cache parts...")

if os.path.exists(main_cache_path):
    try:
        with open(main_cache_path, 'r') as f:
            main_cache = json.load(f)
    except Exception:
        main_cache = {}
else:
    main_cache = {}

total_merged = 0

for suffix in ['A', 'B']:
    part_path = os.path.join(SCRIPT_DIR, f"search_cache_part{suffix}.json")
    if os.path.exists(part_path):
        try:
            with open(part_path, 'r') as f:
                part_cache = json.load(f)
            main_cache.update(part_cache)
            print(f"  Successfully merged {len(part_cache)} queries from part {suffix}")
            total_merged += len(part_cache)
            # Remove part file
            os.remove(part_path)
            print(f"  Deleted temp part file: search_cache_part{suffix}.json")
        except Exception as e:
            print(f"  Error merging part {suffix}: {e}")
    else:
        print(f"  Part file {part_path} not found or not written yet.")

if total_merged > 0:
    with open(main_cache_path, 'w') as f:
        json.dump(main_cache, f, indent=2)
    print(f"Saved consolidated search cache with {total_merged} new queries merged. Total keys now: {len(main_cache)}")
else:
    print("No parts were merged.")
