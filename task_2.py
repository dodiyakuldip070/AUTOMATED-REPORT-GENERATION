import pandas as pd
from fpdf import FPDF

# Function to generate PDF report
def generate_pdf_report(data, output_file):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(0, 10, "Data Analysis Report", ln=True, align="C")
    pdf.ln(10)

    # Summary statistics
    pdf.set_font("Arial", size=12) 
    pdf.cell(0, 10, "Summary Statistics:", ln=True)
    pdf.ln(5)

    for column in data.select_dtypes(include=['number']).columns:
        pdf.cell(0, 10, f"{column}:", ln=True)
        pdf.cell(0, 10, f"  Mean: {data[column].mean():.2f}", ln=True)
        pdf.cell(0, 10, f"  Median: {data[column].median():.2f}", ln=True)
        pdf.cell(0, 10, f"  Standard Deviation: {data[column].std():.2f}", ln=True)
        pdf.ln(5)

    # Data preview
    pdf.cell(0, 10, "Data Preview (First 5 Rows):", ln=True)
    pdf.ln(5)
    pdf.set_font("Courier", size=10)

    for index, row in data.head().iterrows():
        row_data = ' | '.join(str(value) for value in row)
        pdf.cell(0, 10, row_data, ln=True)

    pdf.output(output_file)

# Main script
if __name__ == "__main__":
    # Input file
    input_file = r"C:\Users\kuldi\Desktop\CODETECH_IT_SOLUTION_PYTHON INTERNSHIP\task_2\data.csv"
 # Replace with your data file
    output_file = "report.pdf"

    try:
        # Read data
        data = pd.read_csv(input_file)

        # Generate report
        generate_pdf_report(data, output_file)
        print(f"Report generated successfully: {output_file}")

    except Exception as e:
        print(f"Error: {e}")
