# Changelog

All notable changes to **erpnext-gst-print-formats** will be documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [Unreleased]

### Added
- `CONTRIBUTING.md` with GST-specific code style guidelines
- `CHANGELOG.md` for version tracking

## [0.0.1] - 2026-04-01

### Added
- Initial release
- **GST Sales Invoice** print format with CGST/SGST/IGST breakdown and HSN summary table
- **GST Delivery Note** print format with e-Way Bill number and transporter details
- **GST Purchase Order** print format with supplier GSTIN and place of supply
- **GST Payment Receipt** print format with invoice allocation table
- **GST Credit Note** print format for sales returns with reason field
- `hooks.py` with fixtures configuration for print format installation
- `setup.py` for bench installation
- `__init__.py` for Python module structure
- Supports ERPNext v14 and v15
