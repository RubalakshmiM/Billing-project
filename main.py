import xml.etree.ElementTree as ET
itemlist=[]
pricelist=[]
tree=ET.parse("product list.xml")
root=tree.getroot()
for child in root:
    itemlist.append(child.find('name').text)
    pricelist.append(child.find('price').text)
dicti1={}
dicti={}
dicti = dict(zip(itemlist,pricelist))
n=[]
s=int(input(" Enter the total item purchased :"))
for i in range(0,s):
      keyn=input(" Enter the item name:")
      for key ,value in dicti.items():
          if keyn == key:
              dicti1.update({keyn:value})
      if keyn not in dicti:
            x=input(" This item is not in the list ,do yu want to add this item (y/n)")
            if x=='y':
                   price=int(input(" Enter the price you want to add for the item "))
                   dicti1.update({keyn: price})
            else:
               if x=='n':
                    print(" thankyou")
            n.append(keyn)
bill=0
for key,value in dicti1.items():
    quantity=int(input(" The quantity of " +key+ " purchased is = "))
    totalprice=int(quantity*int(value))
    bill=bill+totalprice
    print("Cost of single quantity of "+key+ " is = ",value, " and the totalprice of "+key+ " is =",totalprice)
print(" Overall bill generated is ",bill)





