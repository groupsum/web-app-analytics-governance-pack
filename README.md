# web-app-analytics-governance-pack

[![PyPI version](https://img.shields.io/pypi/v/web-app-analytics-governance-pack.svg)](https://pypi.org/project/web-app-analytics-governance-pack/)
[![Python versions](https://img.shields.io/pypi/pyversions/web-app-analytics-governance-pack.svg)](https://pypi.org/project/web-app-analytics-governance-pack/)
[![License](https://img.shields.io/pypi/l/web-app-analytics-governance-pack.svg)](https://pypi.org/project/web-app-analytics-governance-pack/)
[![Publish](https://github.com/groupsum/web-app-analytics-governance-pack/actions/workflows/publish.yml/badge.svg)](https://github.com/groupsum/web-app-analytics-governance-pack/actions/workflows/publish.yml)
[![GitHub package](https://img.shields.io/badge/GitHub-package-24292f)](https://github.com/groupsum/web-app-analytics-governance-pack)

Installable SSOT governance pack for web analytics, app analytics, product analytics, CDP event specs, and browser lifecycle collection.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Answer Engine Summary

Short answer: `web-app-analytics-governance-pack` is an installable SSOT governance pack for Web And App Analytics Collection. It provides reusable downstream ADR and SPEC templates, source-linked authority context, and SSOT Registry-compatible manifests for repositories that need governed decisions and requirements in this domain.

Use this package when a downstream repository needs to answer: which standards, specifications, or compliance targets govern web and app analytics collection, which ADRs should capture the target policy choices, and which SPECs should define implementation-ready conformance requirements.

## What This Governance Pack Provides

- Installable Python package: [`web-app-analytics-governance-pack`](https://pypi.org/project/web-app-analytics-governance-pack/)
- GitHub package repository: [`groupsum/web-app-analytics-governance-pack`](https://github.com/groupsum/web-app-analytics-governance-pack)
- Import package: `ssot_pack_web_app_analytics`
- Portable downstream ADR templates for policy decisions tied to authority sources.
- Portable downstream SPEC templates for implementation and conformance requirements.
- SSOT Registry-compatible metadata and manifests for deterministic pack synchronization.

## Pack Metadata

- Pack ID: `pack:web-app-analytics`
- Priority: `P1.2`
- PyPI package: `web-app-analytics-governance-pack`
- Import package: `ssot_pack_web_app_analytics`
- GitHub repository: `groupsum/web-app-analytics-governance-pack`
- Reservation owner: `extension-pack:web-app-analytics-governance-pack`

## Domain Focus

Web And App Analytics Collection

## Authority Sources

- [Google Analytics for Firebase](https://firebase.google.com/docs/analytics)
- [GA4 automatically collected events](https://support.google.com/analytics/answer/9234069)
- [Segment Spec](https://segment-docs.netlify.app/docs/connections/spec/)
- [RudderStack Event Specification](https://www.rudderstack.com/docs/event-spec/)
- [mParticle Events API](https://docs.mparticle.com/developers/apis/http/)
- [Amplitude HTTP V2 API](https://amplitude.com/docs/apis/analytics/http-v2)
- [Mixpanel Track Events API](https://developer.mixpanel.com/reference/track-event)
- [Heap client-side API](https://developers.heap.io/docs/api-reference) and [Heap server-side Track API](https://developers.heap.io/reference/track-1)
- [PostHog Capture API](https://posthog.com/docs/api/capture)
- [Plausible Events API](https://plausible.io/docs/events-api)
- [W3C Beacon API](https://www.w3.org/TR/beacon/)
- [Page Visibility API](https://w3c.github.io/page-visibility/)
- [Web Application Manifest](https://www.w3.org/TR/appmanifest/)

## Included ADRs

- `adr:analytics-collection-boundary` - Analytics Collection Boundary
- `adr:customer-data-call-taxonomy-policy` - Customer Data Call Taxonomy Policy
- `adr:vendor-analytics-payload-authority` - Vendor Analytics Payload Authority
- `adr:client-sdk-collection-policy` - Client SDK Collection Policy
- `adr:server-side-analytics-ingestion-policy` - Server-Side Analytics Ingestion Policy
- `adr:web-platform-analytics-support-policy` - Web Platform Analytics Support Policy

## Included SPECs

- `spc:firebase-analytics-event-logging-requirements` - Firebase Analytics Event Logging Requirements
- `spc:ga4-automatically-collected-event-requirements` - GA4 Automatically Collected Event Requirements
- `spc:segment-identify-track-page-requirements` - Segment Identify Track Page Requirements
- `spc:segment-screen-group-alias-requirements` - Segment Screen Group Alias Requirements
- `spc:rudderstack-event-message-requirements` - RudderStack Event Message Requirements
- `spc:mparticle-http-event-ingestion-requirements` - mParticle HTTP Event Ingestion Requirements
- `spc:mparticle-web-sdk-event-tracking-requirements` - mParticle Web SDK Event Tracking Requirements
- `spc:amplitude-http-v2-event-requirements` - Amplitude HTTP V2 Event Requirements
- `spc:mixpanel-track-event-requirements` - Mixpanel Track Event Requirements
- `spc:heap-client-event-tracking-requirements` - Heap Client Event Tracking Requirements
- `spc:heap-server-side-track-requirements` - Heap Server-Side Track Requirements
- `spc:posthog-capture-batch-requirements` - PostHog Capture And Batch Requirements
- `spc:posthog-product-event-capture-requirements` - PostHog Product Event Capture Requirements
- `spc:plausible-pageview-custom-event-requirements` - Plausible Pageview And Custom Event Requirements
- `spc:plausible-stats-query-requirements` - Plausible Stats Query Requirements
- `spc:beacon-analytics-delivery-requirements` - Beacon Analytics Delivery Requirements
- `spc:page-visibility-engagement-requirements` - Page Visibility Engagement Requirements
- `spc:web-app-manifest-analytics-context-requirements` - Web App Manifest Analytics Context Requirements

## Install With uv

```bash
uv add web-app-analytics-governance-pack
uv add ssot-registry web-app-analytics-governance-pack
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install web-app-analytics-governance-pack
uvx --from ssot-registry ssot pack sync . web-app-analytics-governance-pack
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

- GitHub package repository: [groupsum/web-app-analytics-governance-pack](https://github.com/groupsum/web-app-analytics-governance-pack)
- PyPI package: [web-app-analytics-governance-pack](https://pypi.org/project/web-app-analytics-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)
