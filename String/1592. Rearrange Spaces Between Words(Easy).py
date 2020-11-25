class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = [];
        word = "";
        space = 0;
        for c in text:
            if c != " ":
                word += c;
            else:
                if word != "":
                    words.append(word);
                word = "";
                space += 1;
        if word != "":
            words.append(word)
        if len(words) == 1:
            return words[0] + " " * space
        spaceNeed = space / (len(words) - 1);
        ans = (" " * int(spaceNeed)).join(words);
        if space % (len(words) - 1) != 0:
            ans += " " * (space % (len(words) - 1));
        
        return ans