class Solution {
    public boolean containsDuplicate(int[] nums) {
        int l = nums.length;
        boolean op = false;
        HashMap<Integer, Integer> newMap = new HashMap<>();

        for(int i = 0; i < l; i++){
            int value = nums[i];
                if(newMap.containsKey(value)){
                    op = true;
                }else{
                    newMap.put(nums[i], i);
                                        //return false;
                }

        } 
        return op;
    }
}