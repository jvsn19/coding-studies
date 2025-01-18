import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Solution {
    List<Integer> answer = new ArrayList<>();
    HashMap<Integer, List<Integer>> graph = new HashMap<>();
    HashSet<Integer> visited = new HashSet<>();
    int k;

    private void createGraph(TreeNode root) {
        ArrayDeque<TreeNode[]> stack = new ArrayDeque<>();
        stack.add(new TreeNode[] { root, null });

        while (!stack.isEmpty()) {
            TreeNode[] nodes = stack.pollLast();
            TreeNode cur = nodes[0], parent = nodes[1];

            if (cur == null) {
                continue;
            }

            if (parent != null) {
                this.graph.computeIfAbsent(cur.val, x -> new ArrayList<>()).add(parent.val);
                this.graph.computeIfAbsent(parent.val, x -> new ArrayList<>()).add(cur.val);
            }

            stack.addLast(new TreeNode[] { cur.left, cur });
            stack.addLast(new TreeNode[] { cur.right, cur });
        }
    }

    private void dfs(int root, int distance) {
        if (visited.contains(root)) {
            return;
        }

        visited.add(root);

        if (distance == this.k) {
            this.answer.add(root);
            return;
        }

        this.graph.getOrDefault(root, new ArrayList<>()).forEach(next -> {
            dfs(next, distance + 1);
        });
    }

    public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
        this.k = k;
        createGraph(root);
        dfs(target.val, 0);

        return this.answer;
    }
}