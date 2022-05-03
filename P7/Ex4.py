# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import json
from Seq1 import Seq

genes_dict = {"SRCAP": "ENSG00000080603",
              "FRAT1": "ENSG00000165879",
              "ADA": "ENSG00000196839",
              "RNU6_269P": "ENSG00000212379",
              "FXN": "ENSG00000165060",
              "MIR633": "ENSG00000207552",
              "TTTY4": "ENSG00000228296",
              "RBMY2YP": "ENSG00000227633",
              "FGFR3": "ENSG00000068078",
              "KDR": "ENSG00000128052",
              "ANK2": "ENSG00000145362"}
SERVER = 'rest.ensembl.org'
ENDPOINT = "/sequence/id/"
gene_name = input("Insert the name of the gene you want the info for:")
for k,v in genes_dict.items():
    if k == gene_name:
        identifier = v
        key = k
    else:
        pass

PARAMS = identifier + "?content-type=application/json"

print(f"\nConnecting to server: {SERVER}\n")
print(f"URL: {SERVER + ENDPOINT + PARAMS}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", ENDPOINT + PARAMS) #WE DONT PUT SERVER

    # -- Read the response message from the server
    r1 = conn.getresponse()

    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1) #transforma automaticamente el data en intergers o float (lo q corresponde)si son numeros
    #data1 es un diccionarioque tiene todos sus elementos transformados al tipo correspondiente
    # -- Print the received data
    print("Gene: " + key)
    print("Description: " + data1["desc"])
    print("Description: " + data1["seq"])
    s1 = Seq(data1["seq"])
    print(s1.info())
    d = s1.count()
    print(f"Most frequent base: {s1.processing_genes(d)}")





except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
