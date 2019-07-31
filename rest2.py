from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import json
from auth_user import *
from retrieve_stocks import *
from retrieve_stocks_2 import *

def make_app():
  urls = ([
    ("/user/login", userLogin),
    ("/user/getStocks", userGetStocks),
    ("/user/getStocks_2", userGetStocks_2)
  ])
  return Application(urls, debug=True)

class userLogin(RequestHandler):
  def post(self):
    data = json.loads(self.request.body.decode("utf-8"))
    email = data["email"]
    password = data["pwd"]
    response = authenticateUser(email, password)
    print("Email: " + email)
    print("Password: " + password)
    print("Response: " + str(response))
    response_code = -1
    if(response == -1):
      response_code = -1
    else:
      response_code = 0
    responseData = {
      "response_code": response_code,
      "user_id": response
    }
    print(responseData)
    self.write(json.dumps(responseData))


class userGetStocks(RequestHandler):
  def post(self):
    data = json.loads(self.request.body.decode("utf-8"))
    id = data["id"]
    response = getStockData(id)
    response = json.dumps(response)
    self.write(response)


class userGetStocks_2(RequestHandler):
  def post(self):
    data = json.loads(self.request.body.decode("utf-8"))
    id = data["id"]
    response = getStockData_2(id)
    response = json.dumps(response)
    self.write(response)

    
if __name__ == '__main__':
  app = make_app()
  app.listen(8888)
  IOLoop.instance().start()
