export default function appendToEachArrayValue(array, appendString) {
  const arr = [];
  for (const idx in array) {
    if (array.indexOf(idx)) {
      const value = array[idx];
      arr.push(appendString + value);
    }
  }

  return arr;
}
