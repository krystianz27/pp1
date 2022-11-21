file = open("shopping.txt","a")
product = input("Input a product ")
file.write(product + "\n")

file.close()