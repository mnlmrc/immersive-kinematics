import argparse
import json
import urllib.parse
import urllib.request


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://127.0.0.1:8071")
    parser.add_argument("--recording", required=True)
    parser.add_argument("--ordinal", type=int, required=True)
    args = parser.parse_args()
    recording = urllib.parse.quote(args.recording, safe="")
    url = f"{args.base_url.rstrip('/')}/api/recordings/{recording}/datapoints/{args.ordinal}"
    with urllib.request.urlopen(url, timeout=30) as response:
        print(json.dumps(json.load(response), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())