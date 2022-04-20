import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import urlparse, parse_qs


HTML_FOLDER = "./html/"
LIST_SEQUENCES = ["AGCTTTGGACC", "AAACCCCAAAA", "TTATATAGGG", "ATTTTAGAAAA", "GATACAGATACAGATACA", "ATATAT"]

def read_html_file(filename):
    contents = Path(filename).read_text()
    contents = j.Template(contents)
    return contents

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

        url_path = urlparse(self.path)
        path = url_path.path

        if self.path == "/":
            contents = read_html_file("index.html")\
                .render(context={"n_sequences": len(LIST_SEQUENCES)})
        elif path == "/ping":
            contents = read_html_file(path[1:] + ".html").render()
        else:
            contents = "I am the happy server :-)"

        self.send_response(200)  # -- Status line: OK!
        # Open the form1.html file
        # Read the index from the file



        # Generating the response message




        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("localhost", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()