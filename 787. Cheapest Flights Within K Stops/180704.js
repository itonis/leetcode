/**
 * @param {number} n
 * @param {number[][]} flights
 * @param {number} src
 * @param {number} dst
 * @param {number} K
 * @return {number}
 */
var findCheapestPrice = function(n, flights, src, dst, K) {
    if (dst >= n || src >= n) {return -1;}
    if (src == dst) {return 0;}
    
    var adj = [];
    for (let i=0; i<n; i++) {
        adj.push(new Array(n));
    }
    for (let i=0; i<flights.length; i++) {
        adj[flights[i][0]][flights[i][1]] = flights[i][2];
    }
    
    // var visited = new Set();
    var bestCost = Number.MAX_SAFE_INTEGER;
    var queue = new PriorityQ();
    //  Element [node, cost, stops]
    queue.push([src, 0, -1]);
    var u;
    while ((u=queue.pop())) {
        console.log(u);
        if (u[0] == dst) {
            console.log(queue.heap)
            return u[1];
        }
        if (u[2]>=K) continue;
        // if (visited.has(u[0])) continue;
        // visited.add(u[0]);
        for (let i=0; i<n; i++) {
            if (adj[u[0]][i]) {
                queue.push([i, u[1]+adj[u[0]][i], u[2]+1]);
            }
        }
    }
    return -1;
};

class PriorityQ {
    constructor() {
        this.heap = [];
        this.heap.push([-1,-1]);
    }
    
    peak () {
        return this.heap[1];
    }
    
    pop () {
        if (this.heap.length == 1)  return undefined;
        if (this.heap.length == 2)  return this.heap.pop();
        var ret = this.heap[1];
        let tail = this.heap.pop();
        if (this.heap.length == 2)  {
            this.heap[1] = tail;
            return ret;
        }
        if (this.heap.length == 3) {
            if (tail[1] <= this.heap[2][1]) {
                this.heap[1] = tail;
            } else {
                this.heap[1] = this.heap[2];
                this.heap[2] = tail;
            }
            return ret;
        }
        let pos = 1;
        pos = this.heap[pos*2][1]>this.heap[pos*2+1][1] ? pos*2+1 : pos*2;
        while (tail[1] > this.heap[pos][1]) {
            this.heap[Math.floor(pos/2)] = this.heap[pos];
            if (this.heap[pos*2]) {
                if (this.heap[pos*2+1]) {
                    pos = this.heap[pos*2][1]>this.heap[pos*2+1][1] ? pos*2+1 : pos*2;       
                } else {
                    pos = pos*2;
                }
            } else {
                pos = pos*2;
                break;
            }
        }
        this.heap[Math.floor(pos/2)] = tail;
        return ret;
    }
    
    push (element) {
        this.heap.push(element);
        let pos = this.heap.length-1;
        while (element[1] < this.heap[Math.floor(pos/2)][1]) {
            this.heap[pos] = this.heap[Math.floor(pos/2)];
            pos = Math.floor(pos/2);
        }
        this.heap[pos] = element;
    }
}