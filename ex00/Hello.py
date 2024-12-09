ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# your code here

# part of list
ft_list[1] = "World!"

# part of tuple
y = list(ft_tuple)
y[1] = "Turkey!"
ft_tuple = tuple(y)

# part of set
ft_set.remove("tutu!")
ft_set.add("Istanbul!")

# part of dictionaries
ft_dict["Hello"] = "42Istanbul!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
