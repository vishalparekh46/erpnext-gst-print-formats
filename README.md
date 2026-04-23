# 🧾 erpnext-gst-print-formats

> Indian GST-compliant print format library for ERPNext — Sales Invoice, Purchase Order, Delivery Note & more.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Frappe](https://img.shields.io/badge/Frappe-v14%2B-blue)](https://frappe.io)
[![ERPNext](https://img.shields.io/badge/ERPNext-v14%2B-1abc9c)](https://erpnext.com)

---

## ✨ Features

- 🧾 **GST Sales Invoice** — CGST/SGST/IGST breakup, HSN summary table, QR code ready
- 📦 **Delivery Note** — Transporter details, e-Way Bill number field
- 🛒 **Purchase Order** — Supplier GST details, place of supply
- 💳 **Payment Receipt** — Acknowledgement slip with GST reference
- 🏷️ Supports **GSTIN validation** display for buyer & seller
- 🖨️ Clean, print-friendly layouts using **Jinja2 + HTML/CSS**

---

## 📋 Requirements

- ERPNext v14 or v15
- GST module enabled
- Frappe bench setup

---

## ⚙️ Installation

```bash
# Navigate to your frappe-bench directory
cd ~/frappe-bench

# Get the app
bench get-app https://github.com/vishalparekh46/erpnext-gst-print-formats

# Install on your site
bench --site your-site.local install-app erpnext_gst_print_formats

# Run migrations
bench --site your-site.local migrate
```

---

## 🗂️ Available Print Formats

| Format | DocType | Description |
|---|---|---|
| `GST Sales Invoice` | Sales Invoice | Full GST invoice with HSN summary & tax breakup |
| `GST Delivery Note` | Delivery Note | With e-Way Bill & transporter details |
| `GST Purchase Order` | Purchase Order | Supplier GSTIN, place of supply |
| `GST Payment Receipt` | Payment Entry | Acknowledgement with GST reference |

---

## 🛠️ Usage

After installation, go to the relevant DocType (e.g. Sales Invoice), open a submitted document, and select the print format from the **Print** dropdown.

---

## 📁 Project Structure

```
erpnext_gst_print_formats/
├── print_format/
│   ├── gst_sales_invoice/
│   │   └── gst_sales_invoice.html    # Jinja2 template
│   ├── gst_delivery_note/
│   │   └── gst_delivery_note.html
│   ├── gst_purchase_order/
│   │   └── gst_purchase_order.html
│   └── gst_payment_receipt/
│       └── gst_payment_receipt.html
├── hooks.py
└── __init__.py
```

---

## 🤝 Contributing

Pull requests are welcome! To contribute:

1. Fork the repo
2. Create a branch: `git checkout -b feat/new-format`
3. Commit: `git commit -m "feat: add GST e-invoice format"`
4. Open a PR against `main`

---

## 📄 License

MIT — see [LICENSE](LICENSE)

---

## 👤 Author

**Vishal Parekh** — ERPNext & Frappe Developer at [Aavatto](https://aavatto.com)

- GitHub: [@vishalparekh46](https://github.com/vishalparekh46)
- LinkedIn: [vishalparekh46](https://linkedin.com/in/vishalparekh46)
