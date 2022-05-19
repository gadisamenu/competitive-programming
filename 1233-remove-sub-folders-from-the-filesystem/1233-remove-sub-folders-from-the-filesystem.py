class Node:
    def __init__(self):
        self.folders = defaultdict(Node)
        self.isFolder = False
        
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = Node()
        path = []
        ans = []
        def insert(folders:str):
            temp = root
            folders = folders.split("/")
            for folder in folders[1:]:
                temp = temp.folders[folder]
            temp.isFolder = True
            
        def search(root):
            if root.isFolder:
                ans.append("/"+"/".join(path))
                return
            for folder in root.folders:
                path.append(folder)
                search(root.folders[folder])
                path.pop()
            
        for fold in folder:
            insert(fold)
        search(root)
        
        return ans