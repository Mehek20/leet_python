def findMedianSortedArrays(nums1,nums2):
    A,B=nums1,nums2
    total=len(A)+len(B)
    half=total//2
    # We want to sort array of small len so we will check conditions


    if len(A) > len(B):
        A, B = B,A

    l, r=0,len(A)-1
    while True:
        i = (l + r) // 2  # pointing array a mid value
        j = half - i -2   # left partition of B

        Aleft = A[i] if i >= 0 else float("-infinity")
        Aright = A[i + 1] if i < len(A) else float("infinity")
        Bleft = B[j] if j >= 0 else float("-infinity")
        Bright = B[j + 1] if j < len(B) else float("infinity")

        # Checking for correctness of left partition
        if Aleft <= Bright and Bleft <= Aright:
            # odd condition
            if total % 2:
                return min(Aright,Bright)
            # even condition
            return (max(Aleft,Bleft) + min(Aright + Bright)) / 2
        
        elif Aleft > Bright:
            r = i - 1
        # for correct left partition
        else:
            l = i + 1

            




