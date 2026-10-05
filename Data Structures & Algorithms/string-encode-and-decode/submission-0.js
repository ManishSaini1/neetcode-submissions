class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let result = "";
        for (const str of strs) {
            // Append length + delimiter + actual string
            result += str.length + "#" + str;
        }
        return result;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        const result = [];
        let i = 0;

        while (i < str.length) {
            // Find the delimiter '#' starting from index i
            let j = i;
            while (str[j] !== "#") {
                j++;
            }

            // Parse the string length
            const length = parseInt(str.substring(i, j), 10);

            // Move pointer past the '#' symbol
            i = j + 1;

            // Extract the string using the parsed length
            const originalStr = str.substring(i, i + length);
            result.push(originalStr);

            // Move pointer past the extracted string to the next item
            i += length;
        }

        return result;
    }
}