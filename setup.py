from setuptools import setup, find_packages

setup(
    name="erpnext_gst_print_formats",
    version="0.0.1",
    description="Indian GST-compliant print format library for ERPNext",
    author="Vishal Parekh",
    author_email="vishal@aavatto.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[],
)
