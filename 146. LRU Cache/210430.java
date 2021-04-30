class LRUCache {

    private final int capacity;
    private final Map<Integer, Node> map;
    private final DLL dll;
    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.map = new HashMap<>();
        this.dll = new DLL();
    }
    
    public int get(int key) {
        if (map.containsKey(key)) {
            Node node = map.get(key);
            dll.pop(node);
            dll.pushLeft(node);
            return node.v;
        } else {
            return -1;
        }
    }
    
    public void put(int key, int value) {
        if (map.containsKey(key)) {
            Node node = map.get(key);
            dll.pop(node);
            dll.pushLeft(node);
            node.v = value;
        } else {
            Node node = new Node(key, value);
            int size = dll.pushLeft(node);
            if (size > capacity) {
                Node drop = dll.popRight();
                map.remove(drop.k);
            }
            map.put(key, node);
        }
    }
    
    private static class DLL {
        final Node head;
        
        DLL() {
            head = new Node();
            head.prev = head;
            head.next = head;
        }
        
        int size() {
            return head.v;
        }
        
        int pushLeft(Node node) {
            Node next = head.next;
            head.next = node;
            next.prev = node;
            node.prev = head;
            node.next = next;
            head.v = head.v + 1;
            return head.v;
        }
        
        Node peekRight() {
            return head.prev;
        }
        
        Node pop(Node node) {
            Node prev = node.prev;
            Node next = node.next;
            prev.next = next;
            next.prev = prev;
            head.v = head.v - 1;
            return node;
        }
        
        Node popRight() {
            Node right = head.prev;
            pop(right);
            return right;
        }
    }

    private static class Node {
        int k = -1;
        int v = 0;
        Node next = null;
        Node prev = null;

        Node () {};
        Node(int k, int v) {
            this.k = k; 
            this.v = v;
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */