[33mcommit b30cf66691f7e58f6a5a0f5799e8a0216748470f[m[33m ([m[1;36mHEAD[m[33m -> [m[1;32mmaster[m[33m, [m[1;31morigin/master[m[33m)[m
Author: PARNIKA <moolaparnika.15@gmail.com>
Date:   Wed May 27 13:52:02 2026 +0530

    Added product search feature

[1mdiff --git a/main.py b/main.py[m
[1mindex e33d9be..1229969 100644[m
[1m--- a/main.py[m
[1m+++ b/main.py[m
[36m@@ -98,6 +98,32 @@[m [mdef view_cart(user_id):[m
         total += price*quantity[m
         [m
     print("Total cart amount:",total)[m
[32m+[m[41m    [m
[32m+[m[32m# ---------------- SEARCH PRODUCT ----------------[m[41m    [m
[32m+[m[41m    [m
[32m+[m[32mdef search_product():[m
[32m+[m
[32m+[m[32m    keyword = input("Enter Product Name To Search: ")[m
[32m+[m
[32m+[m[32m    query = """[m
[32m+[m[32m    SELECT * FROM products[m
[32m+[m[32m    WHERE product_name LIKE %s[m
[32m+[m[32m    """[m
[32m+[m
[32m+[m[32m    cursor.execute(query, ("%" + keyword + "%",))[m
[32m+[m
[32m+[m[32m    products = cursor.fetchall()[m
[32m+[m
[32m+[m[32m    if products:[m
[32m+[m
[32m+[m[32m        print("\nSearch Results\n")[m
[32m+[m
[32m+[m[32m        for p in products:[m
[32m+[m[32m            print("ID:", p[0], "Name:", p[1],[m
[32m+[m[32m                  "Price:", p[2], "Stock:", p[3])[m
[32m+[m
[32m+[m[32m    else:[m
[32m+[m[32m        print("No Products Found")[m
 [m
 [m
 # ---------------- PLACE ORDER ----------------[m
[36m@@ -244,28 +270,32 @@[m [mwhile True:[m
 [m
                 print("\n----- USER MENU -----")[m
                 print("1 View Products")[m
[31m-                print("2 Add To Cart")[m
[31m-                print("3 View Cart")[m
[31m-                print("4 Place Order")[m
[31m-                print("5 Payment")[m
[31m-                print("6 Order History")[m
[31m-                print("7 Logout")[m
[32m+[m[32m                print("2 Search Product")[m
[32m+[m[32m                print("3 Add To Cart")[m
[32m+[m[32m                print("4 View Cart")[m
[32m+[m[32m                print("5 Place Order")[m
[32m+[m[32m                print("6 Payment")[m
[32m+[m[32m                print("7 Order History")[m
[32m+[m[32m                print("8 Logout")[m
 [m
                 ch = input("Enter Choice: ")[m
 [m
                 if ch == "1":[m
                     view_products()[m
[31m-[m
[32m+[m[41m                    [m
                 elif ch == "2":[m
[31m-                    add_to_cart(user_id)[m
[32m+[m[32m                    search_product()[m
 [m
                 elif ch == "3":[m
[31m-                    view_cart(user_id)[m
[32m+[m[32m                    add_to_cart(user_id)[m
 [m
                 elif ch == "4":[m
[31m-                    total = place_order(user_id)[m
[32m+[m[32m                    view_cart(user_id)[m
 [m
                 elif ch == "5":[m
[32m+[m[32m                    total = place_order(user_id)[m
[32m+[m
[32m+[m[32m                elif ch == "6":[m
                 #     make_payment(user_id,total)[m
                 #     move_to_history(user_id)elif ch == "5":[m
                    if total > 0:[m
[36m@@ -276,10 +306,10 @@[m [mwhile True:[m
                    else:[m
                       print("No order placed yet")[m
 [m
[31m-                elif ch == "6":[m
[32m+[m[32m                elif ch == "7":[m
                     view_order_history(user_id)[m
 [m
[31m-                elif ch == "7":[m
[32m+[m[32m                elif ch == "8":[m
                     print("Thank You For Shopping")[m
                     break[m
 [m
