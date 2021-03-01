        left, right = 0, 0;
        needLen = len(need);
        vaild = 0;
        check = 1;
        ans = n;
        while right < n:
            if s[right] in need and need[s[right]]:
                need[s[right]] -= 1;
                if need[s[right]] == 0:
                    vaild += 1;
            right += 1;
            
            
            while vaild == needLen:
                ans = min(ans, right - left);
                check = 0;
                if s[left] in need:
                    if need[s[left]] == 0:
                        vaild -= 1;
                        need[s[left]] += 1;
                left += 1;
        print(ans)