import webapp2


form = """
<form method = "post"></form>
<imput type="text" name="q">
<imput type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.respons.out.writen(form)
    def post(self):
        self.respons.out.writen(form)
app = webapp2.WSGIApplication(("/", MainPage))