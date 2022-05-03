import http.client
import json
from pathlib import Path
import jinja2 as j

SERVER = 'rest.ensembl.org'

def read_html_file(filename):
    contents = Path(filename).read_text()
    contents = j.Template(contents)
    return contents

def create_request(url, params):
    # Connect with the server
    conn = http.client.HTTPConnection(SERVER)
    # -- Send the request message, using the GET method. We are
    # -- requesting the main page (/)
    try:
        conn.request("GET", url + params)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    # -- Read the response message from the server
    r1 = conn.getresponse()
    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")
    # -- Read the response's body
    data1 = r1.read().decode("utf-8")
    # -- Print the received data
    print(f"CONTENT: {data1}")
    return json.loads(data1)