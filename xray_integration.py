import requests
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
AUTH_URL = os.getenv("AUTH_URL")
IMPORT_URL = os.getenv("IMPORT_URL")

def get_xray_token(client_id, client_secret):
    payload = {
        "client_id": client_id,
        "client_secret": client_secret
    }
    response = requests.post(AUTH_URL, json=payload)
    if response.status_code == 200:
        return response.text.strip('"') 
    else:
        raise Exception(f"Error autenticando con Xray: {response.status_code} {response.text}")

def upload_junit_result(file_path, token):
    xml_result="""<?xml version="1.0" encoding="utf-8"?>
                    <testsuites>
        <testsuite name="pytest" errors="0" failures="0" skipped="0" tests="1" time="62.456" timestamp="2024-12-27T08:43:23.316889-05:00" hostname="DESKTOP-JNVQD19">
        <testcase classname="tests.test_login" name="test_login_successful" time="61.313" />
         </testsuite>
        </testsuites>"""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "text/xml"
    }
    try:
        response = requests.post(IMPORT_URL, headers=headers, data=xml_result)
        
        if response.status_code == 200:
            print("Resultados subidos exitosamente a Xray.")
            print(response.json()) 
        else:
            print(f"Error subiendo resultados a Xray: {response.status_code} {response.text}")
            print(response.request.headers)  
            print(response.request.body)
            raise Exception(f"Error subiendo resultados a Xray: {response.status_code} {response.text}")
    
    except Exception as e:
        print(f"Error al intentar enviar el archivo: {e}")
        

if __name__ == "__main__":
    junit_file = "resultado.xml"
    
    if not os.path.exists(junit_file):
        raise FileNotFoundError(f"El archivo {junit_file} no existe.")

    try:
        token = get_xray_token(CLIENT_ID, CLIENT_SECRET)
        print("Token obtenido exitosamente.")
         

        upload_junit_result(junit_file, token)
    except Exception as e:
        print(f"Error durante la integración con Xray: {e}")
         
