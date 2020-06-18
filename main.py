import xml.etree.ElementTree as ET
itemlist=[]
pricelist=[]
tree=ET.parse("product list.xml")
root=tree.getroot()
for child in root:
    itemlist.append(child.find('name').text)
    pricelist.append(child.find('price').text)
dicti={}
dicti = dict(zip(itemlist,pricelist))
n=[]
s=int(input(" enter the total item:"))
for i in range(0,s):
      key=input(" enter the name:")
      if key not in dicti:
            x=input(" do yu want to add this item in dict (y/n)")
            if x=='y':
                   price=int(input(" enter the price you want to add for the item "))
                   dicti.update({key: price})
            else:
               if x=='n':
                    print(" thankyou")
            n.append(key)
print(dicti)





