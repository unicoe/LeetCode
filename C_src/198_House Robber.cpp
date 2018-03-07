int max(int n, int m){
    if(n > m)
        return n;
    return m;
}

int ans[100000];

int slove(int* nums, int n){

    if(n < 0)
        return 0;

    if(ans[n] >= 0){
        return ans[n];
    }

    ans[n] = max(nums[n]+slove(nums, n-2),slove(nums, n-1));
    return ans[n];
}

int rob(int* nums, int numsSize) {

    if(numsSize <= 0)
        return 0;
    if(numsSize == 1)
        return nums[numsSize-1];

    ans[0] = nums[0];
    ans[1] = max(nums[0],nums[1]);

    for(int i = 2; i <= numsSize-1; ++i){
        ans[i] = max(nums[i]+ans[i-2], ans[i-1]);
    }

    return ans[numsSize-1];
}


