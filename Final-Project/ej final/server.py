import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse
from Seq1 import Seq
import functions as f

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happytest server: It always returns a message saying
        # that everything is ok
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        # Message to send back to the clinet
        if path == "/":
            contents = f.read_html_file("index.html").render()
        elif path == "/listSpecies":
            if arguments == {}:
                n_species = "-1"
            elif arguments != {}:
                n_species = (arguments["number_species"][0])
            PARAMS = "/info/species?content-type=application/json"
            dict_answer = f.create_request(url= "", params=PARAMS)
            list_species = dict_answer["species"]
            list_species = list_species[0:int(n_species)]
            list_species_2 = []
            for l in list_species:
                for k,v in l.items():
                    if k == "display_name":
                        list_species_2.append(v)
            contents = f.read_html_file("list_species.html")\
                .render(context={"species": list_species_2,
                        "n_species": len(list_species_2)})
        elif path == "/karyotype":
            species = (arguments["species"][0])
            REQ = "/info/assembly/"
            PARAMS = "?content-type=application/json"
            dict_answer = f.create_request(url= REQ + species, params=PARAMS)
            karyotype = dict_answer["karyotype"]
            contents = f.read_html_file("karyotype.html") \
                .render(context={"species": species.upper(),
                                 "karyotype": karyotype})
        elif path == "/ping":
            contents = f.read_html_file(path[1:] + ".html").render()
        elif path == "/get":
            n_sequence = int(arguments["n_sequence"][0])
            sequence = LIST_SEQUENCES[n_sequence]
            contents = f.read_html_file(path[1:] + ".html")\
                .render(context = {
                "n_sequence": n_sequence,
                "sequence": sequence
                })
        else:
            pass

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()