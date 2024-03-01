import os
import requests
import json
import csv
from pdf2image import convert_from_path
import pytesseract
from datetime import datetime
import payload
import configurations
import argparse

parser = argparse.ArgumentParser(description="Select the payload for the OCR.")
parser.add_argument("--payload", type=int, help="payload number to use", default=1)
args = parser.parse_args()


# OCR
current_time = datetime.now().strftime("%H:%M:%S")
start_time = datetime.now()
print(f"Starting OCR at {current_time}.")

total_pages = 0
total_documents = 0
current_document = 0

for filename in os.listdir('venv'):
    if filename.endswith('.pdf'):
        total_documents += 1
        full_path = os.path.join('venv', filename)
        images = convert_from_path(full_path)
        total_pages += len(images)
        single_pdf_contents = ""

        for i, image in enumerate(images):
            text = pytesseract.image_to_string(image)
            page_content = f'Page {i + 1}\n{text}'
            single_pdf_contents += page_content
            txt_filename = filename.replace('.pdf', '.txt')
            with open(txt_filename, 'w') as f:
                f.write(single_pdf_contents)

current_time = datetime.now().strftime("%H:%M:%S")
print(
    f"OCR completed at {current_time} for all PDFs in the current directory. From {total_documents} pdfs, {total_pages} pages were generated.")
# LLM
url = "http://100.120.48.74:1234/v1/chat/completions"
headers = {'Content-Type': 'application/json', }
for filename in os.listdir('venv'):
    if filename.endswith('.txt'):
        current_document += 1
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                document_content = f.read()
                document_number = filename.replace('.txt', '')  # Document number is the filename without extension
            print("sending " + document_number)
            # Fetch the requested payload
            if args.payload == 1:
                payload_data = payload.get_payload1(document_content)
            elif args.payload == 2:
                payload_data = payload.get_payload2(document_content)
            elif args.payload == 3:
                payload_data = payload.get_payload3(document_content)
            else:
                print(f"Invalid payload number {args.payload}")
                continue



            response = requests.request("POST", url, headers=headers, data=json.dumps(payload_data))
            response_dict = json.loads(response.text)
            content = json.loads(response_dict['choices'][0]['message']['content'])
            print("received " + document_number + " scan")
            # Fetch the fieldnames and writer_params based on the selected payload config
            if args.payload == 1:
                fieldnames, writer_params = configurations.config1(content, document_number)
            elif args.payload == 2:
                fieldnames, writer_params = configurations.config2(content, document_number)
            elif args.payload == 3:
                fieldnames, writer_params = configurations.config3(content, document_number)
            else:
                print(f"Invalid payload number {args.payload}")
                exit(1)
            with open('scanResults.csv', 'a', newline='') as f:

                fieldnames = fieldnames
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                if f.tell() == 0:
                    writer.writeheader()  # File is empty, write a header
                writer.writerow(writer_params)
                print("wrote " + document_number + " to file")
                # if POST request is successful, delete the corresponding .txt file
                os.remove(filename)
                current_time = datetime.now().strftime("%H:%M:%S")
                total_time = datetime.now() - start_time
                print(f"Finished scanning {current_document} out of {total_documents} documents at {current_time}. "
                      f"Total time: {total_time}")
        except Exception as e:
            print(f"Failed to process file {filename}. Reason: {str(e)}")