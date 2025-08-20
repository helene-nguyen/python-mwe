"""
A class should have only one responsibility, one reason to change.

Example: A InvoiceManager class should only handle billing logic. Report generation should be handled by another class.
"""
class InvoiceManager:
    def calculate_total(self, items):
        return sum(item.price for item in items)

class ReportGenerator:
    def create_report(self, invoice):
        # Code to generate report
        pass


# ====================== Anti pattern ===============================================================
class Invoice:
    """
    This class handles billing, saving data, and PDF generation, making it hard to maintain and modify.
    """
    def calculate_total(self, items):
        return sum(item.price for item in items)

    def save(self):
        # Save data to database
        pass

    def generate_pdf(self):
        # Generate a PDF document
        pass