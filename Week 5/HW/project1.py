def main():
    actual_value = float(input('Enter actual value of your house: $'))
    assessment(actual_value)
    tax(assessment_value)
    show_assessment_value(assessment_value)
    show_property_tax(property_tax)

def assessment(actual_value):
    global assessment_value
    assessment_value = actual_value * .6
    return assessment_value

def tax(assessment_value):
    tax_rate = 72 / 10000
    global property_tax
    property_tax = assessment_value * tax_rate
    return property_tax

def show_assessment_value(assessment_value):
    print(f"The assessment value for your property is: ${assessment_value:,.2f}")

def show_property_tax(property_tax):
    print(f"The property tax for your property is: ${property_tax:,.2f}")

main()