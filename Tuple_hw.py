
# Livel 1

# # Task1
# tpl=()
# print(tpl)


# #task 2

# sisters=("Anna","Luna","Emma","Lia",)
# print(sisters)
# brothers=("Dima","Jon","Tom","James")
# print(brothers)

# # task 3
# siblings=(sisters+brothers)
# print(siblings)

# #task 4
# siblings=len(sisters+brothers)
# print(siblings)

# #task 5
# siblings=("Anna","Luna","Emma","Lia","Dima","Jon","Tom","James")
# family_members=siblings + ( "Olivia", ) + ("Henry",)
# print(family_members)


# Livel 2

# task 1
family_members=("Olivia","Henry","Anna","Luna","Emma","Lia","Dima","Jon","Tom","James")
(mom,dad,sister_1,sister_2,sister_3,sister_4,*brothers)=family_members
print(mom)
print(dad)
print(sister_1)
print(sister_2)
print(sister_3)
print(sister_4)
print(brothers)

#task 2
fruits=('Apples','Pears','Cherry','Kiwi','Lemon','Orange','Banana')
vegetables=('potato','tomato','cucumber','carrot','mushroom','corn')
animal_products=('meat','Skin or Flesh','Milk','Whey','Eggs')
food_stuff_tp=fruits + vegetables + animal_products
print(food_stuff_tp)

#task 3
food_stuff_tp=('Apples','Pears','Cherry','Kiwi','Lemon','Orange','Banana','potato','tomato','cucumber','carrot','mushroom','corn','meat','Skin or Flesh','Milk','Whey','Eggs')
food_stuff_lst=list(food_stuff_tp)
print(food_stuff_lst)

# task 4



# task 5

food_stuff_lst=('Apples', 'Pears', 'Cherry', 'Kiwi', 'Lemon', 'Orange', 'Banana', 'potato', 'tomato', 'cucumber', 'carrot', 'mushroom', 'corn', 'meat', 'Skin or Flesh', 'Milk', 'Whey', 'Eggs') 
print(food_stuff_lst [2:-2])


# task 6 ?
# food_stuff_tp=('Apples', 'Pears', 'Cherry', 'Kiwi', 'Lemon', 'Orange', 'Banana', 'potato', 'tomato', 'cucumber', 'carrot', 'mushroom', 'corn', 'meat', 'Skin or Flesh', 'Milk', 'Whey', 'Eggs') 
# del (food_stuff_tp)
# print(food_stuff_tp)

#task 7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia'in nordic_countries)
print('Iceland'in nordic_countries)
