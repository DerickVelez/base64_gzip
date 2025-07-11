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

with open(supplier_request_path, mode='r', encoding='utf-8' ) as file:
    request_text = file.read()
    
with open(supplier_response_path, mode='r', encoding='utf-8' ) as file:
    response_text = file.read()

gzip_supplier_request = gzip.compress(request_text.encode('utf-8'))
gzip_supplier_response = gzip.compress(response_text.encode('utf-8'))

compressed_supplier_request = base64.b64encode(gzip_supplier_request)
compressed_supplier_response = base64.b64encode(gzip_supplier_response)

json_obj = json.dumps({"flightQueryId": flightQueryId,
               "supplier": supplier,
               "office": office,
               "supplierRequest": compressed_supplier_request.decode('utf-8'),
               "supplierResponse": compressed_supplier_response.decode('utf-8')
               })

currentpath  = os.getcwd()
filepath = os.path.join("jsonfiles",f'{flightQueryId}-{supplier}.json')
os.makedirs('jsonfiles', exist_ok=True)

with open(filepath, mode= 'w', encoding = 'utf-8') as file:
    file.write(json_obj)

pyperclip.copy(json_obj)