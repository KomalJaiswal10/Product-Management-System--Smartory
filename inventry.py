import inventry_db as d


while True:
    user = int(input("Login 1: Customer , 2: Shopkeeper ---- "))
    
    d.drop_table()


    
#----------------------------------------------------Customer--------------------------------------------------------------

    
    if user==1:
        print()
        print("CUSTOMER")
        while True:
            
            
            print("--------------------------------------------------------------------------------------------------")
            uc = int(input("1: View Products , 2: Buy Product , 3: Exit ---- "))


            
#------View Product------------------------------------------------------------------------------------------------------------------------

            
            if uc==1:
                print()
                print("--------------------------------------------------------------------------------------------------")
                print("Product ID","Product Name","Quantity","Price",sep="                 ")
                print("--------------------------------------------------------------------------------------------------")
                d.view_p()
                print()

                
                
                    


#------Buy Product-------------------------------------------------------------------------------------------------------------------------------


            elif uc==2:
                print()
                cid = input("To check product id's Y/N : ")
                if cid.upper()=='Y':
                    print("--------------------------------------------------------------------------------------------------")
                    print("Product ID","Product Name","Quantity","Price",sep="                 ")
                    print("--------------------------------------------------------------------------------------------------")
                    d.view_p()
                    print("--------------------------------------------------------------------------------------------------")
                    print()
                    
                elif cid.upper()=='N':
                    print()
                    pass
                
                else:
                    print("Invalid Input")

                while True:
                    total=0
                    ntotal=0


                                        
                    bp = int(input("Enter the product Id you want to buy : "))
                    
                    Lpid=d.check_pid()
                    if bp in Lpid:


                        

                        
                        t=(bp,)

                        data = d.total_price(t)
                        for i in data:
                            name_p = i[0]
                            paqty = i[1]
                            qty_p = i[2]

                            
                        print("-----------------------------------------------------------------------------------------------------------------------")

                        if paqty == 0:
                            print("Product Out of Stock")
                            print("-----------------------------------------------------------------------------------------------------------------------")


                        else:
                            d.buy_p(t)
                            uqty = int(input("Enter the number of Quntity you want to buy : "))
                            print()
                            print("-----------------------------------------------------------------------------------------------------------------------")

                            

                            price=qty_p*uqty
                            total+=price

                            tt=(bp,name_p,qty_p,uqty,total)
                            d.cust_table(tt)
                            

                            if uqty>paqty:
                                print("Sorry Available Quntity of",name_p,"is",paqty,"...!")
                                print()
                                sb=input("do you want to purchase Y/N : ")
                                print()
                                if sb.upper()=='Y':
                                    upqty = int(input("Enter the valid Quntity : "))
                                    print()
                                    print("-----------------------------------------------------------------------------------------------------------------------")
                                    price=qty_p*upqty
                                    ntotal+=price
                                    ut=(upqty,ntotal,bp)
                                    d.update_qty(ut)

                                
                                elif sb.upper()=='N':
                                    print("Okay...")
                                    print("-----------------------------------------------------------------------------------------------------------------------")
                                    d.delete_cust(t)

                                else:
                                    print("Invalid Input")

                                    
                            elif paqty==0:
                                print("Out of Stock")
                                print("-----------------------------------------------------------------------------------------------------------------------")






                            res = d.ret_bill()
                            for i in res:
                                    cpid = i[0]
                                    cqty = i[3]
                                    ctotal=i[4]

                            new_owner_pqty = paqty - cqty

                            uto=(new_owner_pqty,bp)
                            d.update_qty_owner(uto)




                            bp2=input("Do you want to continue shopping Y/N :" )
                            print()
                            
                            if bp2.upper()=='Y':
                                pass
                            elif bp2.upper()=='N':
                                print()
                                print("Your Bill")
                                print("-------------------------------------------------------------------------------------------------------------------------")
                                print("Product ID","Product Name","Price","Quantity","TotalPrice",sep="                 ")
                                print("-------------------------------------------------------------------------------------------------------------------------")
                                d.bill()

                                print("-------------------------------------------------------------------------------------------------------------------------")

                                
                                    



                                
                                tl=d.total_pay()

                                
                            
                                p="Total Amount"
                                print(p.rjust(65),str(tl).rjust(44))
                                print("-------------------------------------------------------------------------------------------------------------------------")

                                print()
                                by="Thank You for Shopping Visit Again"
                                print(by.center(120))
                                print()
                                print()
                                break
                            
                            else:
                                print("Invalid Input")

                    else:
                        print("Invalid Product ID")
                        print("-------------------------------------------------------------------------------------------------------------------------")


                    
                    
            print("-------------------------------------------------------------------------------------------------------------------------")
            print()
            break
            





        
                
                
##-------------------------------------------Shopkeeper interface---------------------------------------------------------------------

#----Add Product

    elif user==2:
        print()
        print("SHOPKEEPER")
        while True:
            
            print("--------------------------------------------------------------------------------------------------")
            oc = int(input("1: Add New Product , 2:Update/Modify Product , 3: View Product , 4: Exit ---- "))

            if oc==1:
                while True:
                    print("--------------------------------------------------------------------------------------------------")
                    pname = input("Enter Product Name : ")
                    pqty = int(input("Enter Quantity :"))
                    pprice = int(input("Set Product Price : "))

                    
                    data=d.display_p()          
                    if pname in data:
                        print()
                        print("Product Already exists....")
                        print()
                        viewp=input("Want to View Product List Y/N :")
                        if viewp.upper()=='Y':
                            pass
                        else:
                            print("Okay...")
                    else:
                        t=(pname,pqty,pprice)
                        d.add_po(t)

                    print()
                    cap=input("Continue Adding New Product Y/N : ")
                    if cap.upper()=='Y':
                        pass
                    elif cap.upper()=='N':
                        break



                    
            
##-------Update / Modify Product--------------------------------------------------------------------------------------------------------------



            elif oc == 2:
                
                print("--------------------------------------------------------------------------------------------------")
                update_c = int(input("1:Update Existing Product , 2:Delete existing Product ---- "))

                if update_c==1:

                    while True:

                        print("--------------------------------------------------------------------------------------------------")
                        ename = input("Enter Existing Product Name : ")
                        
                        

                        data=d.display_p()
                        if ename.lower() not in data:
                            print()
                            print("No similar product found")

                        else:
                            uqty = int(input("Enter Quantity :"))
                            uprice = int(input("Set Product Price : "))
                            t=(uqty,uprice,ename.lower())
                            d.update_p(t)

                            print()
                            cup=input("Continue Updating Product Y/N : ")
                            if cup.upper()=='Y':
                                pass
                            elif cup.upper()=='N':
                                break
                            

                elif update_c==2:
                    while True:
                        print("--------------------------------------------------------------------------------------------------")
                        dname = input("Enter Product Name you want to delete : ")
                        t=(dname.lower(),)
                        d.delete_p(t)

                        print()
                        cup=input("Continue Deleting Product Y/N : ")
                        if cdp.upper()=='Y':
                            pass
                        elif cup.upper()=='N':
                            break

                else:
                    print("Invalid Input")





                        
##--------View Product-------------------------------------------------------------------------------------------------------------



                  
            elif oc==3:
                print("--------------------------------------------------------------------------------------------------")
                viewc = int(input("1: View all Products , 2:View specific Products ---- : "))
                
                if viewc==1:
                    print("--------------------------------------------------------------------------------------------------")
                    print("Product ID","Product Name","Quantity","Price",sep="                 ")
                    print("--------------------------------------------------------------------------------------------------")
                    d.view_p()
                elif viewc==2:
                    print()
                    spec_p=input("Enter Product Name : ")
                    print("--------------------------------------------------------------------------------------------------")
                    t=(spec_p.lower(),)
                    d.view_spec_p(t)
                else:
                    print("Invalid Input")




##--------Exit-------------------------------------------------------------------------------------------------------------

                    
            elif oc==4:
               print("--------------------------------------------------------------------------------------------------")
               print("Okay....")
               print()
               break
               
                    
##---------------------------------------------------------------------------------------------------------------------

                    
            else:
               print("Invalid Input")

    else:
        print("Invalid Input")

















            
