class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer,Integer> need = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            if (need.containsKey(nums[i])){
                int[] res = new int[]{need.get(nums[i]),i};
                return res;
            }
            need.put(target - nums[i],i);
            
        }
        return new int[]{0,0};
    }
}
