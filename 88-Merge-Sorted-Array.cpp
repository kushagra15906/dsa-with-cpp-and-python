class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int>arr(m+n);
        int k=m+n;
        for(int i=0;i<m;i++){
            arr[i]=nums1[i];
        }
        for(int i=0;i<n;i++){
            arr[i+m]=nums2[i];
        }
        sort(arr.begin(),arr.end());
        for(int i=0;i<k;i++){
            nums1[i]=arr[i];
        }
    }
};