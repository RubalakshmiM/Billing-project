import xml.etree.ElementTree as ET
tree=ET.parse("product list.xml")
root=tree.getroot()
itemList=[]
n=int(input(" enter the total items:"))
for i in range(0,n):
  a=input(" enter name of the item:")
  itemList.append(a)
dict={}
for x in root.findall('item'):
    for storedItems in itemList:
        if storedItems==x.find('name').text:
            dict[storedItems]=x.find('price').text
bill=0
for key,value in dict.items():
    quantity=int(input(" The quantity of " +key+ " purchased  is  = "))
    totalprice=int(quantity * int(value))
    bill=bill+totalprice
    print(" Cost of single quantity of "+key+ " is =  ",value, " and  the total price of "+key+" is  = ",totalprice  )
print(" Overall bill generated is = ",bill)




