class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        
        conformRestaurants = [];
        
        
        conformRestaurants = [];
        for restaurant in restaurants:
            if veganFriendly == 1:
                if (restaurant[2] == veganFriendly) and (restaurant[3] <= maxPrice) and (restaurant[4] <= maxDistance):
                    conformRestaurants.append(restaurant);
            else:
                if (restaurant[3] <= maxPrice) and (restaurant[4] <= maxDistance):
                    conformRestaurants.append(restaurant);
        
        conformRestaurants = list(sorted(conformRestaurants, key = lambda id : id[0]));
        conformRestaurants = list(reversed(sorted(conformRestaurants, key = lambda rate : rate[1])));
        ans = [];
        for restaurant in conformRestaurants:
            ans.append(restaurant[0]);
        
        return ans;