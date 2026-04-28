# Contributing to erpnext-gst-print-formats

Thanks for your interest in contributing! This project aims to provide high-quality, GST-compliant print formats for the Indian ERPNext community.

## Reporting Bugs

- Open an issue describing the problem, ERPNext version, and steps to reproduce
- Attach a screenshot of the incorrect print output if possible

## Suggesting New Formats

- Open an issue with the DocType name and a sample of what the format should look like
- Reference the relevant GST rule or government notification if applicable

## Submitting a Pull Request

1. Fork the repo and create a branch:
   ```bash
   git checkout -b feat/gst-credit-note-format
   ```

2. Follow the existing file structure:
   ```
   erpnext_gst_print_formats/print_format/<format_name>/<format_name>.html
   ```

3. Use Jinja2 templating — keep logic minimal in the template
4. Test on ERPNext v14 and v15 if possible
5. Commit using Conventional Commits:
   ```
   feat(print-format): add GST credit note format
   fix(sales-invoice): correct IGST column alignment
   ```
6. Open a PR against `main` with a clear description

## Code Style

- HTML templates should be clean and print-friendly
- Use inline CSS only (no external stylesheets)
- Always include GSTIN fields for both buyer and seller
- Always include HSN/SAC codes in item tables

## Questions?

Open an issue or reach out via [discuss.frappe.io](https://discuss.frappe.io)
