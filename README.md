# ssot-pack-web-app-analytics

Installable SSOT governance pack for web analytics, app analytics, product analytics, CDP event specs, and browser lifecycle collection.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Pack Metadata

- Pack ID: `pack:web-app-analytics`
- Priority: `P1.2`
- PyPI package: `ssot-pack-web-app-analytics`
- Import package: `ssot_pack_web_app_analytics`
- GitHub repository: `groupsum/web-app-analytics-governance-pack`
- Reservation owner: `extension-pack:ssot-pack-web-app-analytics`

## Domain Focus

Web And App Analytics Collection

## Authority Sources

- Google Analytics for Firebase
- GA4 automatically collected events
- Segment Spec
- RudderStack Event Specification
- mParticle Events API
- Amplitude HTTP V2 API
- Mixpanel Track Events API
- Heap APIs
- PostHog Capture API
- Plausible Events API
- W3C Beacon API
- Page Visibility API
- Web Application Manifest

## Included ADRs

- `adr:analytics-collection-boundary` - Analytics Collection Boundary
- `adr:customer-data-call-taxonomy-policy` - Customer Data Call Taxonomy Policy
- `adr:vendor-analytics-payload-authority` - Vendor Analytics Payload Authority
- `adr:client-sdk-collection-policy` - Client SDK Collection Policy
- `adr:server-side-analytics-ingestion-policy` - Server-Side Analytics Ingestion Policy
- `adr:web-platform-analytics-support-policy` - Web Platform Analytics Support Policy

## Included SPECs

- `spc:firebase-app-analytics-contract` - Firebase App Analytics Contract
- `spc:cdp-event-spec-contract` - CDP Event Spec Contract
- `spc:product-analytics-ingestion-contract` - Product Analytics Ingestion Contract
- `spc:browser-lifecycle-analytics-contract` - Browser Lifecycle Analytics Contract

## Install With uv

```bash
uv add ssot-pack-web-app-analytics
uv add ssot-registry ssot-pack-web-app-analytics
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install ssot-pack-web-app-analytics
uvx --from ssot-registry ssot pack sync . ssot-pack-web-app-analytics
uv run ssot adr list .
uv run ssot spec list .
```

## Programmatic Usage

```python
from ssot_pack_web_app_analytics import load_document_manifest

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
```

## Resources

- GitHub repository: https://github.com/groupsum/web-app-analytics-governance-pack
- PyPI package: https://pypi.org/project/ssot-pack-web-app-analytics/
- SSOT Registry: https://pypi.org/project/ssot-registry/
