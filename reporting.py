# Funcationality for generating report (CSV)
import csv


def generate_report(data):
    print('Start Generating', data)
    with open('courses_report.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Description", "Price", "Is Private"])
        for course in data:
            writer.writerow(course)
