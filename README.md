# web-app-analytics-governance-pack

<!-- readme-standards:begin branding -->
<p align="center"><a href="https://github.com/groupsum/readme-standards"><img src="https://raw.githubusercontent.com/groupsum/readme-standards/master/docs/assets/readme-standards.svg" alt="Groupsum README Standards" width="300"></a></p>
<p align="center"><strong>web-app-analytics-governance-pack</strong></p>
<p align="center">Installable SSOT governance pack for web analytics, app analytics, product analytics, CDP event specs, and browser lifecycle collection.</p>
<p align="center">
<a href="https://pypi.org/project/web-app-analytics-governance-pack/"><img alt="pypi: web-app-analytics-governance-pack" src="https://img.shields.io/pypi/v/web-app-analytics-governance-pack?labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/pyproject.toml"><img alt="Source version: 0.2.0.dev2" src="https://img.shields.io/static/v1?label=Source%20version&amp;message=0.2.0.dev2&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/pyproject.toml"><img alt="Python: &gt;=3.10,&lt;3.15" src="https://img.shields.io/static/v1?label=Python&amp;message=%3E%3D3.10%2C%3C3.15&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/pyproject.toml"><img alt="Layer: governance" src="https://img.shields.io/static/v1?label=Layer&amp;message=governance&amp;labelColor=1E293B&amp;color=6D28D9"></a>
<a href="https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/README.md#lifecycle-and-migration"><img alt="Lifecycle: active" src="https://img.shields.io/static/v1?label=Lifecycle&amp;message=active&amp;labelColor=1E293B&amp;color=166534"></a>
<a href="https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/static/v1?label=License&amp;message=Apache-2.0&amp;labelColor=1E293B&amp;color=86198F"></a>
<a href="https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/README.md#notices"><img alt="Notice: not required" src="https://img.shields.io/static/v1?label=Notice&amp;message=not%20required&amp;labelColor=1E293B&amp;color=475569"></a>
</p>
<p align="center">
<a href="https://pypi.org/project/web-app-analytics-governance-pack/"><img alt="Monthly PyPI downloads: web-app-analytics-governance-pack" src="https://img.shields.io/pypi/dm/web-app-analytics-governance-pack?labelColor=1E293B&amp;color=0E7490"></a>
<a href="https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/README.md"><img alt="README hits: web-app-analytics-governance-pack" src="https://hits.sh/github.com/groupsum/web-app-analytics-governance-pack/README.md.svg?label=README%20hits&amp;labelColor=1E293B&amp;color=0E7490"></a>
</p>
<p align="center">
<a href="https://github.com/groupsum/web-app-analytics-governance-pack/actions/workflows/readme-standards.yml"><img alt="README standards: CI gate" src="https://img.shields.io/static/v1?label=README%20standards&amp;message=CI%20gate&amp;labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/web-app-analytics-governance-pack/actions/workflows/readme-standards.yml"><img alt="Tests: package and example checks" src="https://img.shields.io/static/v1?label=Tests&amp;message=package%20and%20example%20checks&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/README.md#certification-status"><img alt="Certification: not certified" src="https://img.shields.io/static/v1?label=Certification&amp;message=not%20certified&amp;labelColor=1E293B&amp;color=92400E"></a>
<a href="https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/docs/governance/pack-authoring-guide.md"><img alt="Governance: pack governance" src="https://img.shields.io/static/v1?label=Governance&amp;message=pack%20governance&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/web-app-analytics-governance-pack/actions/workflows/readme-standards.yml"><img alt="Evidence: README and wheel checks" src="https://img.shields.io/static/v1?label=Evidence&amp;message=README%20and%20wheel%20checks&amp;labelColor=1E293B&amp;color=6D28D9"></a>
</p>
<p align="center"><a href="#overview">Overview</a> · <a href="#installation">Installation</a> · <a href="#quick-start">Quick Start</a> · <a href="#usage">Usage</a> · <a href="#public-api-and-import-surfaces">API</a> · <a href="#contributing">Contributing</a> · <a href="#governance">Governance</a> · <a href="#license">License</a></p>
<!-- readme-standards:end branding -->

---

## Overview

### Summary

Installable SSOT governance pack for web analytics, app analytics, product analytics, CDP event specs, and browser lifecycle collection.

### Why This Package

Use this package when a downstream repository needs to answer: which standards, specifications, or compliance targets govern web and app analytics collection, which ADRs should capture the target policy choices, and which SPECs should define implementation-ready conformance requirements.

### When to Use

Use this pack when a downstream SSOT Registry needs reusable decisions and requirements for Web And App Analytics Collection.

### Features

**Included ADRs**

- [`adr:analytics-collection-boundary`](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/src/ssot_pack_web_app_analytics/templates/adr/ADR-1001-analytics-collection-boundary.yaml) — Analytics Collection Boundary
- [`adr:customer-data-call-taxonomy-policy`](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/src/ssot_pack_web_app_analytics/templates/adr/ADR-1002-customer-data-call-taxonomy-policy.yaml) — Customer Data Call Taxonomy Policy
- [`adr:vendor-analytics-payload-authority`](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/src/ssot_pack_web_app_analytics/templates/adr/ADR-1003-vendor-analytics-payload-authority.yaml) — Vendor Analytics Payload Authority
- [`adr:client-sdk-collection-policy`](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/src/ssot_pack_web_app_analytics/templates/adr/ADR-1004-client-sdk-collection-policy.yaml) — Client SDK Collection Policy
- [`adr:server-side-analytics-ingestion-policy`](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/src/ssot_pack_web_app_analytics/templates/adr/ADR-1005-server-side-analytics-ingestion-policy.yaml) — Server-Side Analytics Ingestion Policy
- [`adr:web-platform-analytics-support-policy`](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/src/ssot_pack_web_app_analytics/templates/adr/ADR-1006-web-platform-analytics-support-policy.yaml) — Web Platform Analytics Support Policy
- [`adr:analytics-payloads-use-canonical-beacon-transport`](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/src/ssot_pack_web_app_analytics/templates/adr/ADR-1007-analytics-payloads-use-canonical-beacon-transport.yaml) — Analytics Payloads Use Canonical Beacon Transport

**Included SPECs**

- [`spc:firebase-analytics-event-logging-requirements`](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/src/ssot_pack_web_app_analytics/templates/specs/SPEC-2001-firebase-analytics-event-logging-requirements.yaml) — Firebase Analytics Event Logging Requirements
- [`spc:ga4-automatically-collected-event-requirements`](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/src/ssot_pack_web_app_analytics/templates/specs/SPEC-2002-ga4-automatically-collected-event-requirements.yaml) — GA4 Automatically Collected Event Requirements
- [`spc:segment-identify-track-page-requirements`](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/src/ssot_pack_web_app_analytics/templates/specs/SPEC-2003-segment-identify-track-page-requirements.yaml) — Segment Identify Track Page Requirements
- [`spc:segment-screen-group-alias-requirements`](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/src/ssot_pack_web_app_analytics/templates/specs/SPEC-2004-segment-screen-group-alias-requirements.yaml) — Segment Screen Group Alias Requirements
- [`spc:rudderstack-event-message-requirements`](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/src/ssot_pack_web_app_analytics/templates/specs/SPEC-2005-rudderstack-event-message-requirements.yaml) — RudderStack Event Message Requirements
- [`spc:mparticle-http-event-ingestion-requirements`](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/src/ssot_pack_web_app_analytics/templates/specs/SPEC-2006-mparticle-http-event-ingestion-requirements.yaml) — mParticle HTTP Event Ingestion Requirements
- [`spc:mparticle-web-sdk-event-tracking-requirements`](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/src/ssot_pack_web_app_analytics/templates/specs/SPEC-2007-mparticle-web-sdk-event-tracking-requirements.yaml) — mParticle Web SDK Event Tracking Requirements
- [`spc:amplitude-http-v2-event-requirements`](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/src/ssot_pack_web_app_analytics/templates/specs/SPEC-2008-amplitude-http-v2-event-requirements.yaml) — Amplitude HTTP V2 Event Requirements
- [`spc:mixpanel-track-event-requirements`](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/src/ssot_pack_web_app_analytics/templates/specs/SPEC-2009-mixpanel-track-event-requirements.yaml) — Mixpanel Track Event Requirements
- [`spc:heap-client-event-tracking-requirements`](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/src/ssot_pack_web_app_analytics/templates/specs/SPEC-2010-heap-client-event-tracking-requirements.yaml) — Heap Client Event Tracking Requirements
- [`spc:heap-server-side-track-requirements`](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/src/ssot_pack_web_app_analytics/templates/specs/SPEC-2011-heap-server-side-track-requirements.yaml) — Heap Server-Side Track Requirements
- [`spc:posthog-capture-batch-requirements`](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/src/ssot_pack_web_app_analytics/templates/specs/SPEC-2012-posthog-capture-batch-requirements.yaml) — PostHog Capture And Batch Requirements
- [`spc:posthog-product-event-capture-requirements`](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/src/ssot_pack_web_app_analytics/templates/specs/SPEC-2013-posthog-product-event-capture-requirements.yaml) — PostHog Product Event Capture Requirements
- [`spc:plausible-pageview-custom-event-requirements`](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/src/ssot_pack_web_app_analytics/templates/specs/SPEC-2014-plausible-pageview-custom-event-requirements.yaml) — Plausible Pageview And Custom Event Requirements
- [`spc:plausible-stats-query-requirements`](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/src/ssot_pack_web_app_analytics/templates/specs/SPEC-2015-plausible-stats-query-requirements.yaml) — Plausible Stats Query Requirements
- [`spc:page-visibility-engagement-requirements`](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/src/ssot_pack_web_app_analytics/templates/specs/SPEC-2017-page-visibility-engagement-requirements.yaml) — Page Visibility Engagement Requirements
- [`spc:web-app-manifest-analytics-context-requirements`](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/src/ssot_pack_web_app_analytics/templates/specs/SPEC-2018-web-app-manifest-analytics-context-requirements.yaml) — Web App Manifest Analytics Context Requirements
- [`spc:analytics-beacon-payload-profile`](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/src/ssot_pack_web_app_analytics/templates/specs/SPEC-2019-analytics-beacon-payload-profile.yaml) — Analytics Beacon Payload Profile

### Non-Goals

The pack supplies governance records. A downstream application implements the controls and collects its own conformance evidence.

---

## Getting Started

### Prerequisites

Use Python `>=3.10,<3.15`. Downstream synchronization also requires SSOT Registry and permission to write the target registry.

### Installation

If the desired PyPI release is a prerelease, use its exact version in the installer command.

#### uv

<!-- readme-standards:begin installation.uv -->
```bash
uv add web-app-analytics-governance-pack
```
<!-- readme-standards:end installation.uv -->

#### pip

<!-- readme-standards:begin installation.pip -->
```bash
python -m pip install web-app-analytics-governance-pack
```
<!-- readme-standards:end installation.pip -->

#### Poetry

<!-- readme-standards:begin installation.poetry -->
```bash
poetry add web-app-analytics-governance-pack
```
<!-- readme-standards:end installation.poetry -->

### Quick Start

#### Example

<!-- readme-standards:begin example.quick-start -->
Source: [examples/quick_start.py](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/examples/quick_start.py).

```python
"""Inspect the installed pack identity."""

from ssot_pack_web_app_analytics import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:web-app-analytics"
print(metadata["origin"]["id"])
```
<!-- readme-standards:end example.quick-start -->

#### Expected Result

The script prints `pack:web-app-analytics` from the installed pack metadata.

---

## Usage

### Common Workflows

<!-- readme-standards:begin example.usage -->
Source: [examples/usage.py](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/examples/usage.py).

```python
"""Find a specification and its downstream path in the installed manifest."""

from ssot_pack_web_app_analytics import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:firebase-analytics-event-logging-requirements"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2001-firebase-analytics-event-logging-requirements.yaml"
```
<!-- readme-standards:end example.usage -->

Use the downstream environment that has both SSOT Registry and `web-app-analytics-governance-pack` installed. Inspect the pack and preflight the target registry before approving synchronization.

```bash
uv run ssot pack inspect ssot_pack_web_app_analytics
uv run ssot pack preflight . ssot_pack_web_app_analytics --all
uv run ssot pack sync . ssot_pack_web_app_analytics --all --trust --yes
uv run ssot validate .
```

### Configuration

Select the installed import package `ssot_pack_web_app_analytics` in SSOT Registry. Review reservation owner `extension-pack:web-app-analytics-governance-pack` and the target's trust policy before syncing.

### Error Handling

If preflight reports a schema, trust, or document-number conflict, resolve it in the target registry and repeat preflight before synchronization.

### Best Practices

Pin the pack version in downstream projects. Reference document IDs in local governance and inspect the change set before granting trust.

---

## Package Boundary

### What It Owns

Removed duplicate Beacon mechanics and added an analytics payload profile.

### Public API and Import Surfaces

Import `load_pack_metadata`, `load_document_manifest`, and `read_packaged_document_text` from `ssot_pack_web_app_analytics` to inspect packaged records.

### Entry Points

<!-- readme-standards:begin entry-points -->
This package declares no command-line, GUI, or plugin entry points in its manifest.
<!-- readme-standards:end entry-points -->

### Injected Dependencies

The package binds its metadata and document loaders through `ssot-pack-contracts`. The caller supplies the target registry to SSOT Registry when synchronizing.

### Protocol Consumers

SSOT Registry uses the pack metadata, document manifests, and bundled templates during inspect, preflight, and sync.

### Extensions

Define downstream policies as local records and reference the pack's document IDs. Send proposed changes to the canonical pack through repository review.

---

## Operations and Readiness

### Operational Requirements

Local inspection reads installed package resources. Synchronization requires an initialized downstream registry and explicit operator approval.

### Health and Observability

Review the preflight and sync output, then use `ssot validate` to check the resulting registry.

### Security and Resource Limits

Implicit trust is disabled. Review the exact distribution, version, records, and reserved IDs before enabling trust in a target registry.

### Compatibility

- Python `>=3.10,<3.15`
- SSOT Registry schema `>=0.4.0`
- SSOT pack contracts `>=0.2.17,<0.3.0`

---

## Verification

### Tests

Run `python -m unittest discover -s tests -v` with the pack installed. The [README workflow](https://github.com/groupsum/web-app-analytics-governance-pack/actions/workflows/readme-standards.yml) checks the source README and runs both examples against an installed wheel.

### Certification Status

The pack has no external certification. Downstream adoption requires evidence for the controls an application implements.

### Evidence

See the [README workflow](https://github.com/groupsum/web-app-analytics-governance-pack/actions/workflows/readme-standards.yml) for package and documentation verification and the [packaged records](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/src/ssot_pack_web_app_analytics/templates) for document-level sources.

---

## FAQ

### Why

**Why do document IDs matter?** Downstream records use them to trace an adopted decision or requirement to the pack that owns it.

### How

**How do I preview changes?** Use the registry's pack preflight before approving a sync.

### When

**When should I upgrade?** Read the changelog and preflight the new version against the target registry before applying it.

---

## Documentation and Related Packages

### More Documentation

See the [Pack guide](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/docs/pack-guide.md), [changelog](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/CHANGELOG.md), and [pack metadata](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/src/ssot_pack_web_app_analytics/metadata.json).

### Related Packages

[SSOT Registry](https://pypi.org/project/ssot-registry/) manages downstream registries. [SSOT Pack Contracts](https://pypi.org/project/ssot-pack-contracts/) provides the shared pack interface.

### Project Links

<!-- readme-standards:begin project-links -->
- [Homepage](https://github.com/groupsum/web-app-analytics-governance-pack)
- [Issues](https://github.com/groupsum/web-app-analytics-governance-pack/issues)
- [Repository](https://github.com/groupsum/web-app-analytics-governance-pack)
- [pypi: web-app-analytics-governance-pack](https://pypi.org/project/web-app-analytics-governance-pack/)
<!-- readme-standards:end project-links -->

---

## Contributing

### How to Contribute

Open an [issue](https://github.com/groupsum/web-app-analytics-governance-pack/issues) or pull request describing the affected records, their authority, and the expected downstream effect.

### Development Setup

Install the checkout with `python -m pip install -e .`, then run `python -m unittest discover -s tests -v`. On Python 3.11 or newer, run `uvx --from readme-standards==0.1.3 readme-standards check`.

### Notes for Maintainers

Keep source links, document identifiers, and committed manifest hashes aligned. Run `uvx --from readme-standards==0.1.3 readme-standards render --write` after changing generated README inputs.

---

## Governance

### Ownership and Decision Making

Groupsum maintains `pack:web-app-analytics`. The pack's reservation owner is `extension-pack:web-app-analytics-governance-pack`. Downstream registry operators approve synchronization.

### Standards and Policies

**Authority Sources**

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

### Lifecycle and Migration

Review [release changes](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/CHANGELOG.md) and preflight the chosen version against each downstream registry.

---

## License and Attribution

### License

<!-- readme-standards:begin license -->
Licensed under `Apache-2.0`. See [LICENSE](https://github.com/groupsum/web-app-analytics-governance-pack/blob/master/LICENSE).
<!-- readme-standards:end license -->

### Notices

<!-- readme-standards:begin notices -->
No separate NOTICE file is declared. Review the license and bundled third-party attributions.
<!-- readme-standards:end notices -->
