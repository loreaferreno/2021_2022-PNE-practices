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
        if path == "/listSpecies":
            n_species = arguments["number_species"]
            PARAMS = "?content-type=application/json"
            dict_answer = f.create_request(path, params=PARAMS)
            list_species = dict_answer["species"]
            list_species = list_species[0:n_species]
            content = f.read_html_file("html/list_species.html")\ #falta crear el html de la nueva ventana que muestre la lista
                .render(context={"species": list_species})
        elif path == "/ping":
            contents = f.read_html_file(path[1:] + ".html").render()
        elif path == "/get":
            n_sequence = int(arguments["n_sequence"][0])
            sequence = LIST_SEQUENCES[n_sequence]
            contents = read_html_file(path[1:] + ".html")\
                .render(context = {
                "n_sequence": n_sequence,
                "sequence": sequence
            })
        elif path == "/gene":
            gene_name = arguments["gene_name"][0]
            sequence = Path("./sequences/" + gene_name + ".txt").read_text()
            contents = read_html_file(path[1:] + ".html") \
                .render(context={
                "gene_name": gene_name,
                "sequence": sequence
            })
        elif path == "/operation":
            sequence = arguments["sequence"][0]
            operation = arguments["operation"][0]
            s1 = Seq(sequence)
            if operation == "rev":
                contents = read_html_file(path[1:] + ".html") \
                    .render(context={
                    "operation": operation,
                    "result": s1.reverse()
                })
            elif operation == "info":
                contents = read_html_file(path[1:] + ".html") \
                    .render(context={
                    "operation": operation,
                    "result": info_operation(sequence)
                })
            elif operation == "comp":
                contents = read_html_file(path[1:] + ".html") \
                    .render(context={
                    "operation": operation,
                    "result": s1.complement()
                })
            elif operation == "add":
                contents = read_html_file(path[1:] + ".html") \
                    .render(context={
                    "operation": operation,
                    "result": s1.adding()
                })
        else:
            contents = "I am the happy server! :-)"

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