import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse
from Seq1 import Seq
import functions as f
import json as json


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
            contents = f.read_html_file("html/index.html").render()
        elif path == "/listSpecies":
            contents = f.list_species(arguments)
        elif path == "/karyotype":
            contents = f.karyotype(arguments)
        elif path == "/chromosomeLength":
            contents = f.chromosome_length(arguments)
        elif path == "/geneSeq":
            contents = f.gene_seq(arguments)
        elif path == "/geneInfo":
            contents = f.gene_info(arguments)
        elif path == "/geneCalc":
            contents = f.gene_calc(arguments)
        elif path == "/geneList":
            contents  = f.gene_list(arguments)
        else:
            contents = f.read_html_file("html/error.html") \
                .render(context={})

        self.send_response(200)  # -- Status line: OK!
            # Generating the response message
        if "json" in arguments.keys() and arguments["json"] == ['1']:
            if contents == {}:
                contents = {"There has been an": "ERROR :("}
            contents = json.dumps(contents)
            self.send_header('Content-Type', 'application/json')

            # Define the content-type header:
        else:
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