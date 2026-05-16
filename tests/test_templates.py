from __future__ import annotations

import unittest

from ssot_pack_web_app_analytics import (
    __pypi_package_name__,
    __ssot_package_name__,
    load_document_manifest,
    load_pack_manifest,
    load_pack_metadata,
    load_pack_schema_version,
    read_packaged_document_text,
)


class GovernancePackManifestTests(unittest.TestCase):
    def test_pack_metadata_contract_is_exposed(self) -> None:
        metadata = load_pack_metadata()
        self.assertEqual("ssot-pack-web-app-analytics", __ssot_package_name__)
        self.assertEqual("ssot-pack-web-app-analytics", __pypi_package_name__)
        self.assertEqual("1.0.0", metadata["schema_version"])
        self.assertEqual("ssot-pack-web-app-analytics", metadata["ssot_package_name"])
        self.assertEqual("pack:web-app-analytics", metadata["origin"]["id"])
        self.assertEqual("ssot_pack_web_app_analytics", metadata["origin"]["import_name"])
        self.assertEqual("governance-pack", metadata["origin"]["kind"])
        self.assertEqual("extension-pack", metadata["trust"]["origin"])
        self.assertEqual("extension-pack:ssot-pack-web-app-analytics", metadata["trust"]["reservation_owner"])
        self.assertFalse(metadata["trust"]["trusted_by_default"])
        self.assertEqual("1.0.0", load_pack_schema_version())

    def test_pack_manifest_contract_is_exposed(self) -> None:
        manifest = load_pack_manifest()
        self.assertEqual("ssot-pack-web-app-analytics", manifest["metadata"]["origin"]["package_name"])
        self.assertEqual(2, len(manifest["documents"]["adr"]))
        self.assertEqual(4, len(manifest["documents"]["spec"]))

    def test_packaged_documents_are_readable(self) -> None:
        adr_manifest = load_document_manifest("adr")
        spec_manifest = load_document_manifest("spec")
        self.assertEqual("adr:web-app-analytics-provider-boundary", adr_manifest[0]["id"])
        self.assertEqual("spc:firebase-app-analytics-contract", spec_manifest[0]["id"])
        self.assertIn("Web And App Analytics Collection", read_packaged_document_text("adr", adr_manifest[0]["filename"]))
        self.assertIn("Web And App Analytics Collection", read_packaged_document_text("spec", spec_manifest[0]["filename"]))


if __name__ == "__main__":
    unittest.main()
