from suds.client import Client
#pip install suds-py3
url = "http://localhost:8088/mockApiPortSoap11?wsdl"
client = Client(url)
register_call = client.service.registerCall("Jakub")
results = client.service.results("Jakub")
print("Register_call:")
print("Name: "+register_call.name)
print("Note: "+register_call.note)

print("Results:")
print('\n'.join(results))


