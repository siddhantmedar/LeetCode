/*
// Definition for Employee.
class Employee {
public:
    int id;
    int importance;
    vector<int> subordinates;
};
*/

class Solution {
    unordered_map<int, Employee*> m;
    int dfs(int id){
        int result = m[id]->importance;
        for(auto& z:m[id]->subordinates){
            result+=dfs(z);
        }
        return result;
    }
public:
    int getImportance(vector<Employee*> employees, int id) {
        for(auto& x: employees){
            m[x->id] = x;
        }
        return dfs(id);
    }
};