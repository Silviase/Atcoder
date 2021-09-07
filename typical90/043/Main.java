import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int H = s.nextInt();
        int W = s.nextInt();
        char[][] c = new char[H][W];
        int[][] d = new int[H][W];
        int rs = s.nextInt()-1;
        int cs = s.nextInt()-1;
        int rt = s.nextInt()-1;
        int ct = s.nextInt()-1;

        for (int i = 0; i < H; i++) {
            String str = s.next();
            for (int j = 0; j < W; j++) {
                c[i][j] = str.charAt(j);
                d[i][j] = 10000000;
            }
        }
        
        d[rs][cs] = 0;
        int[] dr = {-1, 0, 1, 0};
        int[] dc = {0, 1, 0, -1};
        PriorityQueue<Point> pq = new PriorityQueue<Point>(Comparator.comparingInt(Point::getD));
        for (int i = 0; i < 4; i++) {
            pq.add(new Point(rs, cs, 0, i));
        }

        while (!pq.isEmpty()) {
            Point p = pq.poll();
            if (p.isOut(H, W)) continue; // out of range
            if (c[p.x][p.y] == '#') continue; // wall
            if (d[p.x][p.y] < p.d) continue; // already visited
            d[p.x][p.y] = p.d;
            for (int i = 0; i < 4; i++) {
                pq.add(new Point(p.x + dr[i], p.y + dc[i], i == p.m? p.d: p.d + 1, i));
            }
        }
        System.out.println(d[rt][ct]);
    }
}

class Point {
    public int x, y, d, m;
    
    Point(int x, int y, int d, int m){
        this.x = x;
        this.y = y;
        this.d = d; 
        this.m = m;
    }

    public int getD() {
        return d;
    }

    public boolean isOut(int H, int W) {
        return x < 0 || x >= H || y < 0 || y >= W;
    }
}