import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from repository import all, create, delete, retrieve, update


class HandleRequests(BaseHTTPRequestHandler):
    '''handles the fetch functions'''

    def parse_url(self, path):
        '''Just like splitting a string in JavaScript. If the path is "/animals/1", the resulting list will have "" at index 0, "animals" at index 1, and "1" at index 2.'''

        path_params = path.split("/")
        resource = path_params[1]
        id = None

        # Try to get item at index 2
        try:
            id = int(path_params[2])
        except IndexError:
            pass
        except ValueError:
            pass

        return (resource, id)

    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_GET(self):
        """Handles GET requests to the server
        """
        response = {}
        self._set_headers(200)
        resource = self.parse_url(self.path)[0]
        id = self.parse_url(self.path)[1]
        if id is not None:
            response = retrieve(resource, id)
        else:
            response = all(resource)
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """Handles POST requests to the server"""

        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize new item
        new_object = {}

        # Add a new animal to the list. Don't worry about
        new_object = create(resource, post_body)

        # Encode the new object and send in response
        self.wfile.write(json.dumps(new_object).encode())

    def do_PUT(self):
        """Handles PUT requests to the server"""
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        update(resource, id, post_body)

        # Encode the new animal and send in response
        self.wfile.write("".encode())

    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_DELETE(self):
        '''delete handler'''
        # Set a 204 response code
        self._set_headers(204)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        delete(resource, id)
        # Delete a single animal from the list
        # Encode the new animal and send in response
        self.wfile.write("".encode())

    # Another method! This supports requests with the OPTIONS verb.

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()


# This function is not inside the class. It is the starting
# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
