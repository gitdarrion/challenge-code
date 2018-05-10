arr = "512 125 928 381 890 90 512 789 469 473 908 990 195 763 102 643 458 366 684 857 126 534 974 875 459 892 686 373 127 297 576 991 774 856 372 664 946 237 806 767 62 714 758 258 477 860 253 287 579 289 496"

arr = arr.split(" ")

arr = [int(e) for e in arr]


def equal(arr):
    # Complete this function
    
    distributions = [1,3,5]
    
    # Insert margin values 
    margins = [0] * (len(arr)-1)
    
    
 
    for i in range(1,len(arr)):
        margin = abs(arr[i-1]-arr[i]) 
        margins[i-1] = margin

    print margins 

    count = 0 
    while sum(margins) > 0:

        print margins
        
        # Get index of max value that is in both 'margin' and 'distributions' arrays.
        max_margin = max(margins)
        max_margin_index = margins.index(max_margin)

        # Get the max value of the two values of chocolate around the margin.
        chocolate_at_margin = [arr[max_margin_index]] + [arr[max_margin_index+1]]
        exclude = max_chocolate_at_margin = max(chocolate_at_margin)
        include = min_chocolate_at_margin = min(chocolate_at_margin)
        
        # Distribute chocolates.
        for i in range(0, len(arr)):
            if arr[i] != exclude: 
                arr[i] += max_margin
        
        print "updated arr: ", arr 

        # Recalculate margins.
        for i in range(1,len(arr)):
            margin = abs(arr[i-1]-arr[i])
            margins[i-1] = margin

      
        
        count += 1

    print count 
        
equal(arr)