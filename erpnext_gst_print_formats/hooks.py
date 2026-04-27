app_name = "erpnext_gst_print_formats"
app_title = "ERPNext GST Print Formats"
app_publisher = "Vishal Parekh"
app_description = "Indian GST-compliant print format library for ERPNext"
app_email = "vishal@aavatto.com"
app_license = "MIT"

# ---------------------------------------------------------------------------
# Print Formats are installed via fixtures
# ---------------------------------------------------------------------------
fixtures = [
    {
        "doctype": "Print Format",
        "filters": [
            ["module", "=", "ERPNext GST Print Formats"]
        ]
    }
]
