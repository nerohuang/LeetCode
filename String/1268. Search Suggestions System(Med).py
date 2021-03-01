class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = [];
        products.sort();
        for i in range(len(searchWord)):
            newProduct = [];
            for product in products:
                if i < len(product) and product[i] == searchWord[i]:
                    newProduct.append(product);
            products = newProduct[::];
            ans.append(products[:3]);
        return ans
    
#我的思路
#一个字节一个字节的找
#如果不符合的就剔除，缩减products的长度

import bisect

#products = ["mobile","mouse","moneypot","monitor","mousepad"]
#searchWord = "mouse"
#products.sort()
#return_list = []
#for i in range(1, len(searchWord) + 1):
#    prefix = searchWord[:i]
#    
#    index = bisect.bisect_left(products, prefix)
#    
#    temp_list = []
#    max_to = min(index + 3,len(products))
#    while index < max_to:
#        if products[index].startswith(prefix):
#            temp_list.append(products[index])
#            index += 1
#        else:
#            break
#    return_list.append(temp_list)

    #更快的做法
    #思路是一样的，不过不用缩减，直接用binary search定位