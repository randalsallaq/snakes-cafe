import textwrap
menu = [
    {
        "appetizers":[
            "Wings",
            "Cookies",
            "Spring Rolls"
        ]
    },
    {
        "Entrees":[
            "Salmon",
            "Steak",
            "Meat Tornado",
            "A Literal Garden"
        ]
    },
    {
        "Desserts":[
            "Ice Cream",
            "Cake",
            "Pie"
        ]
    },
    {
        "Drinks":[
            "Coffee",
            "Tea",
            "Unicorn Tears"
        ]
    }
]







if __name__ == "__main__":
    p = print(textwrap.dedent("""
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
    """))
    
    p = print(textwrap.dedent("""
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls

    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden

    Desserts
    --------
    Ice Cream
    Cake
    Pie

    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears
    """))

    print(textwrap.dedent("""
    
    ***********************************
    ** What would you like to order? **
    ***********************************
    """))

    

    userinput = ''
    amount = {}   

    while userinput != 'quit':
        userinput = input(textwrap.dedent('    > '))
        if userinput in amount:
            amount[userinput]+=1
        else:
            amount[userinput]=1

        if userinput == 'quit':
            print(textwrap.dedent('    Thank You!'))

        else:
            print('** ', amount[userinput], ' orders of ', userinput,' have been added to your meal **')

       
    

    
    
   


