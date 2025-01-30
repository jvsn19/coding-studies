import java.util.ArrayDeque;

class MovingAverage {
    private ArrayDeque<Integer> deque;
    private int size;
    private double sum;

    public MovingAverage(int size) {
        this.deque = new ArrayDeque<>();
        this.size = size;
        this.sum = 0;
    }
    
    public double next(int val) {
        if (this.deque.size() == this.size) {
            this.sum -= this.deque.pollFirst();
        }
        this.deque.offerLast(val);
        this.sum += val;

        return this.sum / this.deque.size();
    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.next(val);
 */