class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        let start = 0,end =numbers.length-1;
        while(start < end){
            const add = numbers[start]+ numbers[end];
            if(add== target){
                return [ start+1, end+1];
            }
            if(add < target){
                start++;
            }
             if(add> target){
               end--;
            }
        }
        return [-1, -1];


    }
}
