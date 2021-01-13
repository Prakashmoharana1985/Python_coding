sales_list = [1, 'ipad', 399.99, 2, 'csble', 29.99]
receipt_list = [round(i*1.065, 2) for i in sales_list if type(i) == float]
print(receipt_list)
