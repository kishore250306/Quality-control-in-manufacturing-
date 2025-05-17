
Import csv
# Define tolerance limits
TARGET_DIAMETER = 50.0 # mm
TOLERANCE = 0.5 # mm
# Sample product measurements
Product_measurements = [
 {product_id: 1, diameter: 50.2},
 {product_id: 2, diameter: 49.6},
 {product_id: 3, diameter: 50.0},
 {product_id: 4, diameter: 50.6}, # Out of spec
 {product_id: 5, diameter: 49.4}, # Out of spec
]
# Function to check tolerance
Def check_tolerance(measured_value):
Return abs(measured_value TARGET_DIAMETER) <= TOLERANCE
# Analyze data and write QC report
Def generate_qc_report(data, filename=qc_report.csv):
 With open(filename, mode=w, newline=) as file:
 Writer = csv.writer(file)
 Writer.writerow([Product ID, Diameter, Status])
 For item in data:
 Status = PASS if check_tolerance(item[diameter]) else FAIL
 Writer.writerow([item[product_id], item[diameter], status])
 Print(fQC report generated: {filename})
# Run QC
Generate_qc_report(product_measurements)
