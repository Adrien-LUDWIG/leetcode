class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        srcs = set()
        dsts = set()

        for src, dst in paths:
            srcs.add(src)
            dsts.add(dst)

        return (dsts - srcs).pop()