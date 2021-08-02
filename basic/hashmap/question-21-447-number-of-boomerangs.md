# 447.回旋镖的数量

~~~typora
给定平面上 n 对 互不相同 的点 points ，其中 points[i] = [xi, yi] 。回旋镖 是由点 (i, j, k) 表示的元组 ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

返回平面上所有回旋镖的数量。

 
示例 1：

输入：points = [[0,0],[1,0],[2,0]]
输出：2
解释：两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
示例 2：

输入：points = [[1,1],[2,2],[3,3]]
输出：2
示例 3：

输入：points = [[1,1]]
输出：0
 

提示：

n == points.length
1 <= n <= 500
points[i].length == 2
-104 <= xi, yi <= 104
所有点都 互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-boomerangs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读



## 思路1：暴力法

暴力法可以理解一下题意

### 代码

~~~python
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        if not points or len(points) <= 2:
            return 0
        res = 0
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                for k in range(len(points)):
                    if k ==i or k == j:
                        continue
                    if self.get_distance(points[i], points[j]) == self.get_distance(points[i], points[k]):
                        res += 1
        return res
    def get_distance(self, x, y):
        return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2
~~~

### 复杂度分析

- 时间复杂度：O(n^3) 3层循环
- 空间复杂度：O(n) 

## 思路2：哈希表

对于每个固定的点维护一个哈希表，因为回旋镖会在意顺序的，不同顺序算是不一样的点，必须遍历两层。对于每个点，距离值为key，这个距离值的点的数量为value

### 代码

```python
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        if not points or len(points) <= 2:
            return 0
        res = 0
        
        for i in range(len(points)):
            hash_map = dict() # 每一个点维护一个哈希表
            for j in range(len(points)):
                dis = self.get_distance(points[i], points[j])
                if dis in hash_map:
                    hash_map[dis] += 1
                else:
                    hash_map[dis] = 1
            for val in hash_map.values():
                res += val * (val-1) # Cn,n-1：如果一个是0，两个是1，多于两个两两组合且有顺序

        return res
    def get_distance(self, x, y):
        return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2
```

### 复杂度分析

- 时间复杂度：O(n^2) 2层循环
- 空间复杂度：O(n) 




