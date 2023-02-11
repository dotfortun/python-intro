import operator

# let someVar = "Some value";
some_var = "Some value"

# // Numbers
# let someInteger = 1
# let someFloat = 1 / 2
some_int: int = 1
some_float: float = 1.0
some_complex: complex = 1.0 + 1j

# print(some_int)
# print(some_float)
# print(some_complex)

# // Strings
# let someString = "This is a normal string."
# let someOtherString = 'This string uses single quotes.'
# let someStringLiteral = `String literals are special.
# They support break returns, and they allow you to do string formatting:
# For example, 1/2 is equal to ${1 / 2}.`

some_str: str = "This is a string."
some_hlf_str: str = 'This is also a string.'
multi_string: str = """

This is a string with a lot of whitespace.
"""
multi_hlf_string = '''This string has less whitespace.'''

f_string: str = f"This is an f string, and you can put variables in it: {some_complex}."
# print(f_string)

# // Booleans
# let someTrueValue = true
# let someFalseValue = false

truthy_value: bool = True
falsy_value: bool = False

# // Arrays
# const books = [
#     {
#         title: "Neuromancer",
#         author: "William Gibson",
#         year_published: 1984,
#         isbn: "",
#         rating: 100
#     },
#     {
#         title: "Snow Crash",
#         author: "Neal Stephenson",
#         year_published: 1992,
#         isbn: "978-01336162-0",
#         rating: 100
#     },
#     {
#         title: "Altered Carbon",
#         author: "Richard K. Morgan",
#         year_published: 2002,
#         isbn: "",
#         rating: 100
#     },
#     {
#         title: "Cryptonomicon",
#         author: "Neal Stephenson",
#         year_published: 2000,
#         isbn: "978-0-380-78862-0",
#         rating: 95
#     }
# ]

some_list: list = [
    "First value",
    "Second value",
    "Third value",
    "Fourth value",
    "Fifth value",
]

# // for (let i=0
#         i < books.length
#         i++) {
#     // console.log(books[i].title)
#     // console.log(books[i].author)
#     // console.log(books[i].year_published)
#     // console.log(books[i].isbn)
#     // console.log(books[i].rating)
#     // console.log('-----')
#     // }

# print(some_list[0])
# for item in some_list:
#     print(item)

# print(some_list)

# for i in range(100):
#     print(i)

# // Objects
# let snowCrash = {
#     title: "Snow Crash",
#     author: "Neal Stephenson",
#     year_published: 1992,
#     isbn: "978-01336162-0",
#     rating: 100
# }

snow_crash: dict = {
    "title": "Snow Crash",
    "author": "Neal Stephenson",
    "year_published": 1992,
    "isbn": "978-01336162-0",
    "rating": 100
}

# print(snow_crash["title"])

# // Null/Undefined
# let someNull = null
# let someUndefined = undefined

some_none = None

# const crypto = {
#     title: "Cryptonomicon",
#     author: "Neal Stephenson",
#     year_published: 2000,
#     isbn: "978-0-380-78862-0",
#     rating: 95
# }

# // console.log(crypto.ibsn)

# //Functions
# const someFunction = (someArgument) = > {
#     // This is the body of the function.
#     return someArgument
# }


def some_func():
    print("This is inside the scope of the function!")


# const sum = (arrayOfNumbers) = > {
#     let result = 0
#     for (let i=0
#          i < arrayOfNumbers.length
#          i++) {
#         result += arrayOfNumbers[i]
#     }
#     return result
# }

def sum(*args, op=operator.add):
    """
    sum(1, 2, 3, 4, 5, 6) = 21
    sum(1, 2, 3, 4, 5, 6, op=operator.mul) = 720
    """
    items = list(args)
    x = items.pop()
    for y in items:
        x = op(x, y)
    return x


def collatz(some_argument):
    if not some_argument % 2:
        return some_argument / 2
    else:
        return 3 * some_argument + 1


# print(sum(1, 2, 3, 4, 5, 6))
# print(sum(1, 2, 3, 4, 5, 6, op=operator.mul))
# print(sum(1, 2, 3, 4, 5, 6, op=lambda x, y: x ** y))
# print(collatz(5))

# // If/else if/else
# for (let i = 0; i < 10; i++) {
#   if (i < 5) {
#     console.log("i is less than 5!", i);
#   } else if (i < 9) {
#     console.log("i is still less than 9.", i);
#   } else {
#     console.log("i is equal to 9!", i);
#   }
# }


pets = [
    {
        "name": "Sombra",
        "age": 0.5,
        "color": "black",
        "is_awake": False,
        "is_affectionate": True,
    }, {
        "name": "Grizelle",
        "age": 5,
        "color": "brown",
        "is_awake": True,
        "is_affectionate": True,
    }, {
        "name": "Maxi",
        "age": 4,
        "color": "brown ombre",
        "is_awake": True,
        "is_affectionate": True,
    }, {
        "name": "Dexter",
        "age": 7,
        "color": "black",
        "is_awake": False,
        "is_affectionate": True,
    },
    {
        "name": "Bazel",
        "age": 2.5,
        "color": "light brown",
        "is_awake": True,
        "is_affectionate": True,
    }
]

# for pet in pets:
#     if pet["is_awake"]:
#         print(f"""{pet["name"]} is awake!""")
#     elif not pet["is_awake"]:
#         print(f"""{pet["name"]} is not awake!""")

#     if pet["age"] < 3:
#         print(f"""{pet["name"]} is younger than 3.""")
#     elif pet["age"] < 6:
#         print(f"""{pet["name"]} is younger than 6.""")
#     else:
#         print(f"""{pet["name"]} is older than 6.""")

# //Ternary operator
# // condition ? value if true : value if false
# let someHTML = `<h2>${pet.name ? pet.name : "No pet selected."}</h2>`

something: str = "Sombra is awake!" if pets[0]["is_awake"] else "Sombra is napping."
# print(something)


# List comprehension
names_comp: list = [pet["name"] for pet in pets]
# print(names_comp)

pet_names = []
for pet in pets:
    pet_names.append(pet["name"])
# print(pet_names)
