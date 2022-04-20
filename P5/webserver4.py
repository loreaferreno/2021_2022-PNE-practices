import http.server
import socketserver
import termcolor
from pathlib import Path

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

        request_line = self.requestline.split(" ")
        method = request_line[0]
        path = request_line[1]
        status = request_line[2]

        # IN this simple server version:
        # We are NOT processing the client's request
        if path == "/":
        # Message to send back to the clinet
            contents = Path("index.html").read_text()
            self.send_response(200)  # -- Status line: OK!
        elif path.endswith("html"):
            file = path[1:]
            try:
                contents = Path(file).read_text()
                self.send_response(200)
            except FileNotFoundError:
                contents = Path("error.html").read_text()
                self.send_response(404)

        else:
            contents = Path("error.html").read_text()
            self.send_response(404)


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