class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums) - 1;
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red];
                red += 1;
                white += 1;
            elif nums[white] == 1:
                white += 1;
            elif nums[white] == 2:
                nums[blue], nums[white] = nums[white], nums[blue];
                blue -= 1;


#This is a dutch partitioning problem. We are classifying the array into four groups: red, white, unclassified, and blue. 
#Initially we group all elements into unclassified. We iterate from the beginning as long as the white pointer is less than the blue pointer.
#
#If the white pointer is red (nums[white] == 0), we swap with the red pointer and move both white and red pointer forward. 
#If the pointer is white (nums[white] == 1), the element is already in correct place, so we don't have to swap, just move the white pointer forward. 
#If the white pointer is blue, we swap with the latest unclassified element.


#four solution
#// one pass in place solution
#void sortColors(int A[], int n) {
#    int n0 = -1, n1 = -1, n2 = -1;
#    for (int i = 0; i < n; ++i) {
#        if (A[i] == 0) 
#        {
#            A[++n2] = 2; A[++n1] = 1; A[++n0] = 0;
#        }
#        else if (A[i] == 1) 
#        {
#            A[++n2] = 2; A[++n1] = 1;
#        }
#        else if (A[i] == 2) 
#        {
#            A[++n2] = 2;
#        }
#    }
#}
#
#// one pass in place solution
#void sortColors(int A[], int n) {
#    int j = 0, k = n - 1;
#    for (int i = 0; i <= k; ++i){
#        if (A[i] == 0 && i != j)
#            swap(A[i--], A[j++]);
#        else if (A[i] == 2 && i != k)
#            swap(A[i--], A[k--]);
#    }
#}
#
#// one pass in place solution
#void sortColors(int A[], int n) {
#    int j = 0, k = n-1;
#    for (int i=0; i <= k; i++) {
#        if (A[i] == 0)
#            swap(A[i], A[j++]);
#        else if (A[i] == 2)
#            swap(A[i--], A[k--]);
#    }
#}