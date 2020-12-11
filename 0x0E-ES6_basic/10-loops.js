export default function appendToEachArrayValue(array, appendString) {
  const arr = [];
  for (const value in array) {
    arr.push(appendString + value);
  }

  return arr;
}
