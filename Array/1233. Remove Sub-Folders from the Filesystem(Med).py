#class Solution:
#    def removeSubfolders(self, folders: List[str]) -> List[str]:
#        dirs = set()
#        folders = sorted(list(filter(None,folder.split('/'))) for folder in folders)
#        for folder_fp in folders:
#            curr_name = ""
#            for folder in folder_fp:
#                curr_name += f"/{folder}"
#                if curr_name in dirs:
#                    break
#            else:
#                dirs.add(curr_name)
#        return dirs

#思路其实就是先把所有文件夹切割，然后依次相加，如果发现重复的就跳过，如果没有就加
#入

