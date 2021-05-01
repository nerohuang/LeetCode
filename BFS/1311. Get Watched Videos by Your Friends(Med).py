class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        queue = [(id, 0)];
        
        seen = set([id]);
        videos = [];
        
        while queue:
            current, dis = queue.pop(0);
            if dis == level:
                videos += watchedVideos[current];
            
            seen.add(current);
            
            for f in friends[current]:
                if f not in seen:
                    queue.append((f, dis + 1));
            
            if dis > level:
                break;
        
        return [k for k,v in sorted(Counter(videos).items(), key = lambda x: (x[1],x[0]))]


# 一个十分典型的BFS问题

# 其实bfs问题就是要怎么处理深度，还有已经遍历过的node
# 以后要记得用set之类的。
# 如果懂了思路就很简单了。建立一个queue存入给出的id作为root
# 然后深度为0，建立一个seen表示遍历过的id，然后videos来存
# 那一深度id看过的videos
# 然后就是bfs的思路做就可以了。。
# 最后统计videos里面看的最多的就行了。