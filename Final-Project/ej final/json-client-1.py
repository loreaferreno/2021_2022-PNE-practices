# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
def connection(ENDPOINT, PARAMS):
    try:
        conn.request("GET", ENDPOINT + PARAMS)
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
    return data1

ENDPOINT = input("Please introduce the desired endpoint: ")
PARAMS = input("Please introduce the desired parameters: ")
data1 = connection(ENDPOINT, PARAMS)
print(data1)

#Here I leave some examples so it is easier to check if it is functioning
# ENDPOINTS: /listSpecies , /chromosomeLength , /geneList
# PARAMS: ?number_species=12&json=1 , ?species=dog&chromosome=20&json=1 , ?chromo=1&start=22125500&end=22136000&json=1
