#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

#define MAXSIZE 300
#define INF 0x3f3f3f3f

int p[MAXSIZE];
int caminho[MAXSIZE];
int distancia[MAXSIZE];
int adj[MAXSIZE][MAXSIZE];

int dijkstra(int, int);
void reverso(int *, int);

int __size;

int main(int argc, char **argv)
{

    int n, m, a, b, w, d;

    while (scanf("%d %d", &n, &m), n && m)
    {

        for (int i = 0; i <= n; ++i)
            for (int j = 0; j <= n; ++j)
                adj[i][j] = INF;

        for (int i = 0; i < m; ++i)
        {

            scanf("%d %d %d", &a, &b, &w);
            adj[a][b] = adj[b][a] = w;

        }

        scanf("%d", &d);
        int ans = dijkstra(d, n);

        if (ans <= 120)
            printf("Will not be late. ");
        else
            printf("It will be %d minutes late. ", ans - 120);

        printf("Travel time - %d - best way -", ans);

        for (int i = 0; i <= __size; ++i)
            printf(" %d", caminho[i]);

        printf("\n");

    }
    return 0;

}

int dijkstra(int d, int size)
{

    memset(p, -1, sizeof(p));
    bool vis[MAXSIZE] = { false };
    for (int i = 0; i <= size; ++i)
        distancia[i] = INF;
    p[d] = d;
    distancia[d] = 0;
    for (int i = 0; i <= size; ++i)
    {
        int v = -1;
        for (int j = 0; j <= size; ++j)
            if (!vis[j] && (v == -1 || distancia[j] < distancia[v]))
                v = j;
        if (distancia[v] == INF)
            break;
        vis[v] = true;
        for (int j = 0; j <= size; ++j)
            if (distancia[v] + adj[v][j] < distancia[j])
                distancia[j] = adj[v][j] + distancia[v], p[j] = v;
    }

    int u = 1;
    __size = 0;
    while (p[u] != u)
        caminho[__size++] = u, u = p[u];
    caminho[__size] = d;
    reverso(caminho, __size + 1);
    return distancia[1];

}

void reverso(int *v, int n)
{

    for (int i = 0, j = n - 1; i < j; ++i, --j)
    {

        int tmp = v[i];
        v[i] = v[j];
        v[j] = tmp;

    }

}