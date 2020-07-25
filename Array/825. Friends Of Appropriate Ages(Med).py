class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ans = 0;
        ages.sort();
        for age in ages:
            left = bisect.bisect(ages, 0.5 * age + 7);
            right = bisect.bisect(ages, age);
            ans += max(0, right - left - 1);
        return ans;

#from collections import Counter
#class Solution:
#    # use a hashset or array which key is the age, and value is the count
#    # number of people could go billions, but the cardinality of ages is 120
#    # Time: O(n) for building the hash, O(120*120) for checking the friend request
#    def numFriendRequests(self, ages: List[int]) -> int:
#       counter = Counter(ages)
#       result = 0
#       for age0 in counter:
            for age1 in counter:
                if age1 <= age0 < 2 * age1 - 14:
                    result += counter[age0] * counter[age1]
                    if age0 == age1:
                        result -= counter[age0] # exclude self request
#       return result