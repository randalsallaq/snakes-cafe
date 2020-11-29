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
    print("""
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
    """)
    
    print("""
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
    """)

    print("""
    
    ***********************************
    ** What would you like to order? **
    ***********************************
    """)

    userinput = ''
    amount = {}   

    while userinput != 'quit':
        userinput = input('    > ')
        if userinput in amount:
            amount[userinput]+=1
        else:
            amount[userinput]=1

        if userinput == 'quit':
            print('    Thank You!')

        else:
            print('** ', amount[userinput], ' orders of ', userinput,' have been added to your meal **')

       
    

    
    
   


