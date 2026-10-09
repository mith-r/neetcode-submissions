
class Solution {
    public int missingNumber(int[] nums) {
        Set<Integer> numSet = new HashSet<>();

        for (int n:nums){
            numSet.add(n);
        }

        for (int i = 0; i <= numSet.size()+1; i++){

            if (numSet.contains(i) == false){
                return i;
            }
        }
        return 0;
    }
}
