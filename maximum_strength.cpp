#include<bits/stdc++.h>
using namespace std;

struct cell {
    int t, s, x, y;
    cell(int time, int str, int r, int c) {
        t = time;
        s = str;
        x = r;
        y = c;
    }
};

bool cmp(cell a, cell b) {
    if(a.t == b.t) 
        return a.s < b.s;
    return a.t > b.t;
}

int ans_t = -1, ans_s = -1;
void solve(int n, int m, vector<vector<string>> &grid, vector<vector<int>> &tim, int k) {
    int sx = -1, sy = -1, ex = -1, ey = -1;
    vector<vector<int>> sharks(n, vector<int>(m));
    
    for(int i=0; i<n; i++) {
        for(int j=0; j<m; j++) {
            if(grid[i][j] == "S") 
                sx = i, sy = j;
            else if(grid[i][j] == "D") 
                ex = i, ey = j;
            else 
                sharks[i][j] = stoi(grid[i][j]);
        }
    }
    
    priority_queue<cell, vector<cell>, bool(*)(cell,cell)> q(cmp);
    q.push(cell(0, k, sx, sy));
    map<pair<int,int>, pair<int,int>> vis;
    
    int dx[] = {0,0,1,-1};
    int dy[] = {1,-1,0,0};
    
    while(!q.empty()) {
        auto cur = q.top();
        q.pop();
        int x = cur.x, y = cur.y;
        
        if(vis.count({x,y})) {
            if(vis[{x,y}].first <= cur.t && vis[{x,y}].second >= cur.s)
                continue;
        }
        vis[{x,y}] = {cur.t, cur.s};
        
        if(x == ex && y == ey) {
            ans_t = cur.t;
            ans_s = cur.s;
            return;
        }
        
        for(int i=0; i<4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if(nx < 0 || nx >= n || ny < 0 || ny >= m) 
                continue;
                
            if(cur.s < sharks[nx][ny]) 
                continue;
                
            int ns = cur.s - sharks[nx][ny] - 1;
            if(ns < 0) 
                continue;
                
            q.push(cell(cur.t + tim[nx][ny], ns, nx, ny));
        }
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n, m;
    cin >> n >> m;
    
    vector<vector<string>> grid(n, vector<string>(m));
    vector<vector<int>> tim(n, vector<int>(m));
    
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++) 
            cin >> grid[i][j];
            
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++) 
            cin >> tim[i][j];
            
    int k;
    cin >> k;
    
    solve(n, m, grid, tim, k);
    
    if(ans_t == -1) 
        cout << "Not Possible";
    else 
        cout << ans_t << " " << ans_s;
        
    return 0;
}