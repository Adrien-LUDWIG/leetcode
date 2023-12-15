class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        srcs, dsts = zip(*paths)
        srcs = set(srcs)
        dsts = set(dsts)
        return (dsts - srcs).pop()