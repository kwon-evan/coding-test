class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]],
    ) -> List[float]:
        self.graph = defaultdict(dict)

        for (i, j), v in zip(equations, values):
            self.graph[i][j] = v
            self.graph[j][i] = 1 / v

        return [self.bfs(i, j, set()) or -1.0 for i, j in queries]

    def bfs(self, start, end, visited):
        if start not in self.graph or end not in self.graph:
            return

        queue = [(start, 1)]
        while queue:
            i, v = queue.pop(0)
            if i == end:
                return v
            if i in visited:
                continue
            visited.add(i)
            for j in self.graph[i]:
                queue.append((j, v * self.graph[i][j]))
