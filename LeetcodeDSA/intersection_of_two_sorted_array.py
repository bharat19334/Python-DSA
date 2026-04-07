def intersection(nums1,nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1 & set2)

nums1 = [1,2,3,4,5]
nums2 = [4,5,6,7,9]
print(intersection(nums1,nums2))