class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solutions = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in solutions:
                solutions[key] = []
            solutions[key].append(s)
        return list(solutions.values())