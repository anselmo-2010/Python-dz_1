count = 2
boxSize = 80 * 70 * 50
boxNetto = 40
boxCub = (80/100 * 70/100 * 50/100)
boxBrutto =  boxNetto + 15*40 / 100
transport = int(650 * boxCub) 
totalCount = transport * count
print (f'Стоимость перевозки : {totalCount}сом')


totalSum = 2500000
nalogSum = round(totalSum * 100 / 112, 2)
marjaSum = round(nalogSum * 100 / 130, 2)
netPriceForOne = marjaSum / 2
print(f'Чистая стоимость товара :{netPriceForOne}сом')
print(nalogSum)
print(marjaSum)

dic ={
    'num' : 2,
    'volume' : 0.28,
    'weight_nett': 40,
    'weight_brutto': 46,
    'margin': 515109.89,
    'tax': 267857.14,
    'total_price': 2500000,
}
print(dic)