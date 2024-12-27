def update_test_type_to_generic(test_key, token):
    """
    Actualiza el tipo de un Test Case en Xray a 'Generic'.
    
    :param test_key: Clave del Test Case en Xray (por ejemplo, TCL-123).
    :param token: Token de autenticación obtenido desde Xray.
    """
    url = f"https://xray.cloud.getxray.app/api/v2/test/{test_key}/type"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {"testType": "Generic"}

    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 200:
        print(f"El Test Case {test_key} fue actualizado a 'Generic'.")
    else:
        print(f"Error al actualizar el Test Case {test_key}: {response.status_code} {response.text}")
