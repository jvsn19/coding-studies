import java.util.*;

class Solution {
    class Pair {
        public String node;
        public double val;

        public Pair(String node, double val) {
            this.node = node;
            this.val = val;
        }

        @Override
        public String toString() {
            return String.format("%s %.2f", this.node, this.val);
        }
    }

    private double calculate(String dividend, String divisor, HashMap<String, HashMap<String, Double>> graph) {
        Stack<Pair> stack = new Stack<>();
        HashSet<String> marked = new HashSet<>();
        stack.push(new Pair(dividend, 1.0));
        

        while (!stack.isEmpty()) {
            Pair cur = stack.pop();

            if (divisor.equals(cur.node)) {
                return cur.val;
            }

            if (marked.contains(cur.node)) {
                continue;
            }

            marked.add(cur.node);
            graph.get(cur.node).forEach((dest, val) -> {
                stack.push(new Pair(dest, cur.val * val));
            });

        }

        return -1.0;
    }

    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        HashMap<String, HashMap<String, Double>> graph = new HashMap<String, HashMap<String, Double>>();

        for (int i = 0; i < equations.size(); ++i) {
            String dividend = equations.get(i).get(0);
            String divisor = equations.get(i).get(1);
            double quocient = values[i];

            if (!graph.containsKey(dividend)) {
                graph.put(dividend, new HashMap<String, Double>());
            }
            if (!graph.containsKey(divisor)) {
                graph.put(divisor, new HashMap<String, Double>());
            }

            graph.get(dividend).put(divisor, quocient);
            graph.get(divisor).put(dividend, 1/quocient);
        }

        double[] ans = new double[queries.size()];

        for (int i = 0; i < queries.size(); ++i) {
            String dividend = queries.get(i).get(0);
            String divisor = queries.get(i).get(1);

            if(!graph.containsKey(dividend) || !graph.containsKey(divisor)) {
                ans[i] = -1;
            }

            else {
                ans[i] = calculate(dividend, divisor, graph);
            }
        }

        return ans;
    }
}