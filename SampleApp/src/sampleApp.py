import requests

url = 'http://localhost:8080/AppCore'

def sayHello():
    return requests.get(f"{url}/sayHello").text

def sayName(name):
    return requests.get(f"{url}/sayName/{name}").text

if __name__ == "__main__":

    print(sayHello())
    print(sayName("sampleApp"))