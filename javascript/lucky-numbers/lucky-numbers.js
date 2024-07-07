// @ts-nocheck

/**
 * Calculates the sum of the two input arrays.
 *
 * @param {number[]} array1
 * @param {number[]} array2
 * @returns {number} sum of the two arrays
 */
export function twoSum(array1, array2) {
  return Number(array1.join("")) + Number(array2.join(""));
}

/**
 * Checks whether a number is a palindrome.
 *
 * @param {number} value
 * @returns {boolean} whether the number is a palindrome or not
 */
export function luckyNumber(value) {
  const reversed = [];
  for(let i = 0; i <= String(value).split("").length; i++){
    reversed.unshift(String(value).split("")[i])
  }

  return value == Number(reversed.join(""));
}

/**
 * Determines the error message that should be shown to the user
 * for the given input value.
 *
 * @param {string|null|undefined} input
 * @returns {string} error message
 */
export function errorMessage(input) {
  if(!input){
    return "Required field";
  }

  const n_in = (Number(input) != input )?  0: Number(input)
  return (!n_in) ? "Must be a number besides 0": "";
}
