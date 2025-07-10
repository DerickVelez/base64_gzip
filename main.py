import json
import pyperclip
import os
import base64
import gzip
import xml.etree.ElementTree as ET

flightQueryId = input('Enter Flight Query ID: ')
supplier = input("Enter Supplier: ")
office = input("Enter Office:" )
supplier_request_path = input("Enter Supplier Request: ")
supplier_response_path =  input("Enter Supplier Response: ")

request = ET.parse(rf"{supplier_request_path}")
request_root = request.getroot()
request_text = request_root.text.strip()

response = ET.parse(rf"{supplier_request_path}")
response_root = response.getroot()
response_text = response_root.text.strip()

gzip_supplier_request = gzip.compress(request_text.encode('utf-8'))
gzip_supplier_response = gzip.compress(response_text.encode('utf-8'))

compressed_supplier_request = base64.b64encode(gzip_supplier_request)
compressed_supplier_response = base64.b64encode(gzip_supplier_response)

flight_list = [f"flightQueryId:{flightQueryId}",
               f"supplier: {supplier}",
               f"office: {office}",
               f"supplierRequest: {compressed_supplier_request.decode('utf-8')}",
               f"supplierResponse: {compressed_supplier_response.decode('utf-8')}"
               ]

json_obj = json.dumps(flight_list)

currentpath  = os.getcwd()
filepath = os.path.join("jsonfiles",f'{flightQueryId}-{supplier}.json')

with open(filepath, mode= 'w', encoding = 'utf-8') as file:
    file.write(json_obj)

pyperclip.copy(json_obj)