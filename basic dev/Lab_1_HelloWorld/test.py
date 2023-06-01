import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):  # Why get() - This methods is called when HTTP GET request is made to root URL
        # After calling, it simple returns 'Hello World' text on Web Page
        self.response.write("Hello World!")


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)