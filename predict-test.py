#!/usr/bin/env python
# coding: utf-8

import requests


url = 'http://localhost:9090/predict'

student_id = 'my05-2025'
student = {
    "cgpa": 8.1,
    "internships": 1,
    "projects": 2,
    "workshopscertifications": 3,
    "aptitudetestscore": 75,
    "softskillsrating": 4.4,
    "extracurricularactivities": "No",
    "placementtraining": "Yes",
    "ssc_marks": 78,
    "hsc_marks": 69    
}


response = requests.post(url, json=student).json()
print(response)

probability = response['placementstatus_probability']
placementstatus = response['placementstatus']

if placementstatus:
    print(f"Student with ID {student_id} has a likelihood of placement of {probability:.2f}.")
else:
    print(f"Student with ID {student_id} needs support. The likelihood of placement is {probability:.2f}.")