#自動販売機_電子マネー処理ver.

class DrinkItem:
  def info(self):
    if self.stock > 0:
      print("【　"+ str(self.number)+"　】"+ self.name +"　：　¥"+ str(self.price))
    else:
      pass

menu_drink1 = DrinkItem()
menu_drink1.number = 1
menu_drink1.name = "コーラ"
menu_drink1.price = 160
menu_drink1.stock = 10

menu_drink2 = DrinkItem()
menu_drink2.number = 2
menu_drink2.name = "ポカリスエット"
menu_drink2.price = 160
menu_drink2.stock = 10

menu_drink3 = DrinkItem()
menu_drink3.number = 3
menu_drink3.name = "ミネラルウォーター"
menu_drink3.price = 100
menu_drink3.stock = 10

menu_drink4 = DrinkItem()
menu_drink4.number = 4
menu_drink4.name = "スパークリングウォーター"
menu_drink4.price = 120
menu_drink4.stock = 10

menu_drink5 = DrinkItem()
menu_drink5.number = 5
menu_drink5.name = "りんごジュース"
menu_drink5.price = 140
menu_drink5.stock = 10

menu_drink6 = DrinkItem()
menu_drink6.number = 6
menu_drink6.name = "コーヒー"
menu_drink6.price = 150
menu_drink6.stock = 10

menu_drink7 = DrinkItem()
menu_drink7.number = 7
menu_drink7.name = "コーンポタージュ"
menu_drink7.price = 130
menu_drink7.stock = 10

menu_drink000 = DrinkItem()
menu_drink000.number = 000
menu_drink000.stock = 0

#辞書を作って数値からとってくる
drink_items = {
1 : menu_drink1,  2 : menu_drink2,   3 : menu_drink3,  4 : menu_drink4,  5 : menu_drink5,  6 : menu_drink6,  7 : menu_drink7, 000 : menu_drink000
}

#↑はリストでも表すことが可能
#　drinkItems = [
#　   menu_drink1,
#　   menu_drink2,
#　   menu_drink3,
#　   menu_drink4,
#　   menu_drink5,
#　   menu_drink6,
#　   menu_drink7,
#　]
#　product_number = int(input("購入を希望する商品番号を数値で教えてください"))
#　chosen_number = drinkItems[product_number - 1]

menu_drink1.info()
menu_drink2.info()
menu_drink3.info()
menu_drink4.info()
menu_drink5.info()
menu_drink6.info()
menu_drink7.info()

while True:
  product_number = int(input("購入を希望する商品番号を数値で入力をお願いします。もし購入を中止する際は、【 000 】と入力をお願いします。>>>"))
  emoney_budget = int(input("電子マネーをタッチしてください。(電子マネーの金額を入力してください)>>>"))
  print("電子マネーの金額>>>"+str(emoney_budget)+"円")

  if product_number == 000:
    print("キャンセルを承りました。購入作業を終了します、ご利用頂きありがとうございました。")
    break
  elif emoney_budget < 99:
    print("電子マネーの残高が少ないため、続けて購入ができません。")
    print("購入作業を終了します、ご利用頂きありがとうございました。")
    break
  elif 0 < product_number < 8:
    print("購入金額は"+ str(drink_items[product_number].price) + "円です。")
    print(str(drink_items[product_number].name)+"を受け取り口よりお取りください。")
    drink_items[product_number].stock = drink_items[product_number].stock - 1
    print(str(drink_items[product_number].name)+"の在庫は"+str(drink_items[product_number].stock)+"本になりました。")
    balance_price = emoney_budget - drink_items[product_number].price
    print("現在の電子マネー残高は" + str(balance_price) + "円です。")
    print("これで購入作業を終了します、ご利用頂きありがとうございました。")
    break
  else:
    print("指定された数値の製品は見当たりません。再度入力してください。")
