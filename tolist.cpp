//convert an adjacency matrix to a adjacency list
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

unordered_map<int, vector<int>> tolist(int N, vector<vector<int>> &paths)
{
    unordered_map<int, vector<int>> graph;
    for (auto &p : paths)
    {
        graph[p[0]].push_back(p[1]);
        // graph[p[1]].push_back(p[0]);
    }

    return graph;
}
int main()
{

    vector<vector<int>> paths;
    paths.push_back({1, 2});
    paths.push_back({1, 3});
    paths.push_back({2, 3});
    paths.push_back({3, 4});

    // paths.push_back({1});

    unordered_map<int, vector<int>> graph = tolist(4, paths);
    // for (int i = 0; i < graph.size(); i++)
    // {
    //     // cout << graph[i] << " ";
    //     // print key here

    //     for (auto &iter : graph[i])
    //     {
    //         cout << iter << " ";
    //     }
    //     cout << endl;
    // }

    for (auto itr = graph.begin(); itr != graph.end(); itr++)
    {
        int key = itr->first;
        vector<int> &values = itr->second;
        cout << key << " ";
        for (auto value : values)
        {
            cout << value << " ";
        }
        cout << endl;
    }
}