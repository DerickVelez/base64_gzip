import json
import pyperclip
import os
import base64
import gzip

flightQueryId = input('Enter Flight Query ID: ')
supplier = input("Enter Supplier: ")
office = input("Enter Office:" )
supplierRequest = input("Enter Supplier Request: ")
supplierResponse =  input("Enter Supplier Response: ")

currentpath  = os.getcwd()
filepath = os.path.join("jsonfiles",f'{flightQueryId}-{supplier}.json')

compressed_supplier_request = base64.b64decode(supplierRequest)
compressed_supplier_response = base64.b64decode(supplierResponse)

decompressed_supplier_request = gzip.decompress(compressed_supplier_request)
decompressed_supplier_response = gzip.decompress(compressed_supplier_response)

flight_list = [f"flightQueryId:{flightQueryId}",
               f"supplier: {supplier}",
               f"office: {office}",
               f"supplierRequest: {decompressed_supplier_request}",
               f"supplierResponse: {decompressed_supplier_response}"
               ]

json_obj = json.dumps(flight_list)
print(json_obj)

with open(filepath, mode= 'w', encoding = 'utf-8') as file:
    file.write(json_obj)

pyperclip.copy(json_obj)