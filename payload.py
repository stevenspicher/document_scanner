def get_payload1(document_content):
    return {
        "messages": [
            {"role": "system",
             "content": f"You are a quick and efficient paralegal assistant."},
            {"role": "user",
             "content": f"For the following text, please provide the document number, "
                        f"grantee, grantor, the filing date, the type of instrument, "
                        f"The legal description of the land, what is being transferred,"
                        f"and any terms: {document_content} "
                        f"Please format the response "
                        f"in a JSON format that can be parsed into a JavaScript object "
                        f"like the following example: "
                        f"'instrument': 'name of instrument or type of document', "
                        f"'grantor': 'name of any listed grantors',"
                        f" 'grantee': 'name of any listed grantees', "
                        f"'fileDate': 'date the document was filed in the courthouse', "
                        f"'legalDescription': 'description of lands involved "
                        f"limited to Township, Range and Section', "
                        f"'transferred': 'any interest or value being transferred', "
                        f"'terms': 'any terms listed'  "
                        f"Do not add additional internal objects or arrays."
                        f"The only fields that should be returned are 'instrument',"
                        f"'grantor', 'grantee', fileDate',"
                        f"'legalDescription', 'transferred', and 'terms'."
                        f"Use proper punctuation, grammar, and spacing for all legal descriptions,"
                        f" property transferred, or terms of the documents, names, or instruments. "
                        f"For Grantors and Grantees, if persons are named in the document as 'husband and wife'"
                        f"or as 'joint tenants' or any other specific relationship, "
                        f"all parties should be listed."
                        f"The Legal Description should be summarized and only include the "
                        f"Townships, Ranges and Sections, "
                        f"and should not include any QTR-QTR portions such as SWSW or N2N2. "
                        f"Format the legal description as follows:"
                        f" Township 32 Range 76 Section 2 "
                        f" or Township 41 Range 12 Section 32"


                        f"Use the following format for the date, if found:"
                        f"mm/dd/yyyy"
                        f"examples:"
                        f"02/28/2001"
                        f"12/25/2020"
                        f"01/01/1999"
             },
        ],
        "temperature": .02,
        "max_tokens": -1,
        "stream": "false"
    }



def get_payload2(document_content, document_number):


    return {
        "messages": [
            {"role": "system",
             "content": f"You are a quick and efficient paralegal assistant."},
            {"role": "user",
             "content": f"For the following text, please provide the "
                        f"grantee, grantor, the filing date, the type of instrument, "
                        f"The legal description of the land, what is being transferred,"
                        f"and any terms: {document_content} "
                        f"Please format the response "
                        f"in a JSON format that can be parsed into a JavaScript object "
                        f"like the following example: "
                        f"'instrument': 'name of instrument or type of document', "
                        f"'grantor': 'name of any listed grantors',"
                        f" 'grantee': 'name of any listed grantees', "
                        f"'fileDate': 'date the document was filed in the courthouse', "
                        f"'legalDescription': 'description of lands involved "
                        f"limited to Township, Range and Section', "
                        f"'transferred': 'any interest or value being transferred', "
                        f"'terms': 'any terms listed'  "
                        f""
                        f"Do not add additional internal objects or arrays."
                        f"The only fields that should be returned are 'instrument',"
                        f"'grantor', 'grantee', fileDate',"
                        f"'legalDescription', 'transferred', and 'terms'."
                        f"Use proper punctuation, grammar, and spacing for all legal descriptions,"
                        f" property transferred, or terms of the documents, names, or instruments. "
                        f"For Grantors and Grantees, if persons are named in the document as 'husband and wife'"
                        f"or as 'joint tenants' or any other specific relationship, "
                        f"all parties should be listed."
                        f"The Legal Description should be summarized and only include the "
                        f"Townships, Ranges and Sections, "
                        f"and should not include any QTR-QTR portions such as SWSW or N2N2. "
                        f"Format the legal description as follows:"
                        f" Township 32 Range 76 Section 2 "
                        f" or Township 41 Range 12 Section 32"


                        f"Use the following format for the date, if found:"
                        f"mm/dd/yyyy"
                        f"examples:"
                        f"02/28/2001"
                        f"12/25/2020"
                        f"01/01/1999"
             }
        ],
        "temperature": .02,
        "max_tokens": -1,
        "stream": "false"
    }

def get_payload3(document_content):
    return {
        "messages": [
            {"role": "system",
             "content": f"You are a quick and efficient paralegal assistant."},
            {"role": "user",
             "content": f"For the following text, please provide the type "
                        f"of instrument: {document_content}"
                        f"Please format the response "
                        f"in a JSON format that can be parsed into a JavaScript object "
                        f"like the following example: "
                        f"'instrument': 'name of instrument or type of document' "
                        f"if an instrument can not be determined, respond with 'undetermined'"
             },
        ],
        "temperature": .02,
        "max_tokens": -1,
        "stream": "false"
    }