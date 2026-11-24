"""Inspect the installed pack identity."""

from ssot_pack_web_app_analytics import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:web-app-analytics"
print(metadata["origin"]["id"])
