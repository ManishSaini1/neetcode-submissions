class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
         s = s.replace(/[^a-zA-Z0-9]/g, '');

        let i=0; 
        let j= s.length -1;
        while(i< j){
            if(s.charAt(i).toLowerCase()== s.charAt(j).toLowerCase()){
                console.log(s.charAt(i));
                i++; j--; continue;
            }else{
                return false
            }
        }
        return true;
    }
}
