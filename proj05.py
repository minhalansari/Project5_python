################################################################################
#Project 5
#Open file function opens the file if its correct
#Revenue function calculates the revenue
#Cost of goods sold function calculates cost of goods sold
#Calculate ROI functions uses revenue and cost of goods sold functions
#main function sorts the products and finds teh best selling ad and best ROI
################################################################################
def open_file():
   
   while True:
        filename = input("Input a file name: ")
        try:
            fp = open(filename, 'r')
            return fp
            
        except FileNotFoundError:
            print("Unable to open file. Please try again.")
            pass
            
def revenue(num_sales, sale_price):
    num_sales = int(num_sales)
    sale_price = float(sale_price)
    revenue = num_sales * sale_price
    return revenue
    #pass

def cost_of_goods_sold(num_ads, ad_price, num_sales, production_cost):
    '''costs of goods sold = advertising total + production total'''
    num_ads = int(num_ads)
    ad_price= float(ad_price) 
    num_sales = int(num_sales)
    production_cost = float(production_cost)
    total_ad = num_ads * ad_price
    production_total = num_sales * production_cost
    cost_of_goods_sold = total_ad + production_total
    return cost_of_goods_sold
    #pass

def calculate_ROI(num_ads, ad_price, num_sales, sale_price, production_cost):
    '''ROI = (Revenue - Cost of goods sold)/Cost of goods sold'''
    ROI = ((revenue(num_sales, sale_price)) - (cost_of_goods_sold(num_ads, ad_price, num_sales, production_cost))) / (cost_of_goods_sold(num_ads, ad_price, num_sales, production_cost))   
    return ROI
    #pass





def main():

    ## open the file
    fp = open_file()
    ## Some print lines to match formatting in Mimir tests
    print()
    print("RobCo AdStats M4000")
    print("-------------------")
    print() 
    previous_product= ''
    max_sale = 0
    max_name = ''
    max_roi= 0
    for line in fp:
        line = line.strip()
        product= line[:27]
        ad_type = line[27:54]
        num_ads = line[54:62]
        ad_price = line [62:70]
        num_sales = line[70:78]
        sale_price = line[79:86]
        production_cost = line[86:94]
        roi = calculate_ROI(num_ads, ad_price,num_sales, sale_price, production_cost)
        print(product)
        if roi > max_roi:
            max_roi = roi 
            max_adtype = ad_type
        if int(num_sales) > int(max_sale):
            max_sale = num_sales     
            max_name = ad_type
            max_num = num_ads
            max_price = ad_price
            max_saleprice= sale_price
            max_pc = production_cost
                 
       
        if product != previous_product:
            print(previous_product)
            #print(num_sales)
            #print("  {:27s}{:>11s}".format("Best-Performing Ad","sales"))
            #print(max_sale)
            previous_product = product
            
            print("  {:27s}{:>11s}".format("Best-Performing Ad",  "sales"))
            print("  {:27s}{:>11s}".format(max_name, max_sale))
            print("  {:27s}{:>11s}".format("Best ROI","percent"))
            print("  {:27s}{:>10.2f}{:>1s}".format(max_adtype, max_roi, "%"))
            max_sale = 0
            max_roi = 0
        else:
            previous_product=product
            #print(num_sales)
            #print(max_sale)
               
        
    
    #print("  {:27s}{:>11s}".format("Best-Performing Ad",  "sales"))
    #print("  {:27s}{:>11d}".format(max_name, max_sale))
    #print("  {:27s}{:>11s}".format("Best ROI", max_adtype, "percent" , max_roi))
    pass  

if __name__ == "__main__":
    main()
