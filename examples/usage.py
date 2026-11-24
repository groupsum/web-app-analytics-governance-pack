"""Find a specification and its downstream path in the installed manifest."""

from ssot_pack_web_app_analytics import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:firebase-analytics-event-logging-requirements"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2001-firebase-analytics-event-logging-requirements.yaml"
