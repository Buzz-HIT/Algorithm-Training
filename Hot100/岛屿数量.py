action = [[1, 0], [0, 1], [-1, 0], [0,-1]]
def dfs(grid, visited, i, j):
        for k in range(4):
            nextx = i + action[k][0]
            nexty = j + action[k][1]
            if nextx >= len(grid) or nextx < 0 or nexty >= len(grid[0]) or nexty < 0:
                continue
            if grid[nextx][nexty] == '1' and visited[nextx][nexty] == False:
                  visited[nextx][nexty] = True
                  dfs(grid, visited, nextx, nexty)
                  



def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    result = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
                # print(grid[i][j], visited[i][j])
                if grid[i][j] == '1' and visited[i][j] == False:
                    # print(grid[i][j], visited[i][j])
                    result += 1
                    visited[i][j] = True
                    dfs(grid, visited, i, j)
    return result

grid = [
  ['1','1','1','1','0'],
  ['1','1','0','1','0'],
  ['1','1','0','0','0'],
  ['0','0','0','0','0']
]
print(numIslands(grid))  