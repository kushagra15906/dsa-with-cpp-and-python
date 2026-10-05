class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int k=nums1.size();
        int l=nums2.size();
        vector<int>arr(k+l);
        for(int i=0;i<k;i++){
            arr[i]=nums1[i];
        }
        for(int i=0;i<l;i++){
            arr[i+k]=nums2[i];
        }
        // int res;
        sort(arr.begin(),arr.end());
        int n=k+l;
        if(n%2==1){
            return arr[n/2];
        }
        else{
            return (arr[n/2]+arr[((k+l)/2)-1])/2.0;
        }
    }
};