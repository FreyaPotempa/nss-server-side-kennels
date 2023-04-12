import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from repository import all

# method_mapper = {
#     "animals": {
#         "all": get_all_animals,
#         "single": get_single_animal},
#     "employees": {
#         "all": get_all_employees,
#         "single": get_single_employee},
#     "customers": {
#         "all": get_all_customers,
#         "single": get_single_customer
#     },
#     "locations": {
#         "all": get_all_locations,
#         "single": get_single_location
#     }
# }


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
        response = all(resource)
        self.wfile.write(json.dumps(response).encode())

    # def do_POST(self):
    #     """Handles POST requests to the server"""

    #     self._set_headers(201)
    #     content_len = int(self.headers.get('content-length', 0))
    #     post_body = self.rfile.read(content_len)

    #     # Convert JSON string to a Python dictionary
    #     post_body = json.loads(post_body)

    #     # Parse the URL
    #     (resource, id) = self.parse_url(self.path)

    #     # Initialize new item
    #     new_animal = None
    #     new_location = None
    #     # new_employee = None
    #     new_customer = None

    #     # Add a new animal to the list. Don't worry about
    #     # the orange squiggle, you'll define the create_animal
    #     # function next.
    #     if resource == "animals":
    #         new_animal = create_animal(post_body)

    #     # Encode the new animal and send in response
    #     self.wfile.write(json.dumps(new_animal).encode())

    #     if resource == "locations":
    #         new_location = create_location(post_body)

    #     self.wfile.write(json.dumps(new_location).encode())

    #     if resource == "customers":
    #         new_customer = create_customer(post_body)

    #     self.wfile.write(json.dumps(new_customer).encode())

    #     if resource == "employees":
    #         new_employee = create_employee(post_body)

    #     self.wfile.write(json.dumps(new_employee).encode())

    # # A method that handles any PUT request.
    # def do_PUT(self):
    #     """Handles PUT requests to the server"""
    #     self._set_headers(204)
    #     content_len = int(self.headers.get('content-length', 0))
    #     post_body = self.rfile.read(content_len)
    #     post_body = json.loads(post_body)

    #     # Parse the URL
    #     (resource, id) = self.parse_url(self.path)

    #     # Delete a single animal from the list
    #     if resource == "animals":
    #         update_animal(id, post_body)

    #     if resource == "customers":
    #         update_customer(id, post_body)

    #     if resource == "employees":
    #         update_employee(id, post_body)

    #     if resource == "locations":
    #         update_location(id, post_body)

    #     # Encode the new animal and send in response
    #     self.wfile.write("".encode())

    # def _set_headers(self, status):
    #     # Notice this Docstring also includes information about the arguments passed to the function
    #     """Sets the status code, Content-Type and Access-Control-Allow-Origin
    #     headers on the response

    #     Args:
    #         status (number): the status code to return to the front end
    #     """
    #     self.send_response(status)
    #     self.send_header('Content-type', 'application/json')
    #     self.send_header('Access-Control-Allow-Origin', '*')
    #     self.end_headers()

    # def do_DELETE(self):
    #     '''delete handler'''
    #     # Set a 204 response code
    #     self._set_headers(204)

    #     # Parse the URL
    #     (resource, id) = self.parse_url(self.path)

    #     # Delete a single animal from the list
    #     if resource == "animals":
    #         delete_animal(id)

    #     if resource == "employees":
    #         delete_employee(id)

    #     if resource == "locations":
    #         delete_location(id)

    #     if resource == "customers":
    #         delete_customer(id)
    #     # Encode the new animal and send in response
    #     self.wfile.write("".encode())

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
