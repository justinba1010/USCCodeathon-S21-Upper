/* Copyright 2021
** Justin Baum
** MIT License
*/

#include <vector>
#include <iostream>
#include <string>
#include <climits>
using namespace std;

vector<string> min_number_of_jumps(vector<int> &array, vector<string> &names) {
    int size = array.size();
    vector<string> solution;
    int steps = array[0];
    int max_reach = array[0];
    int max_index = 0;
    solution.push_back(names[0]);
    for (int i = 1; i < array.size() - 1; i++) {
        int new_reach = i + array[i];
        --steps;
        if (new_reach > max_reach) {
            max_index = i;
            max_reach = new_reach;
        }
        if (steps == 0) {
            solution.push_back(names[max_index]);
            steps = max_reach - i;
        }
    }
    return solution;
}

int main(void) {
    int n;
    cin >> n;
    vector<int> array;
    vector<string> names;
    for(int _ = 0; _ < n; ++_) {
        int x;
        cin >> x;
        array.push_back(x);
    }
    for(int _ = 0; _ < n; ++_) {
        string x;
        cin >> x;
        names.push_back(x);
    }
    auto x = min_number_of_jumps(array, names);
    //cout << x.first << endl;
    for(string name : x) {
        cout << name << " ";
    }
    cout << names[n - 1];
    cout << endl;
    return 0;
}
